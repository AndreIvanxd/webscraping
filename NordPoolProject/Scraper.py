from playwright.sync_api import sync_playwright
import pandas as pd
import sys
import datetime
import sqlite3


def init_db():
    """Initialize a local database."""
    conn = sqlite3.connect("nordpool_prices.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            kuupaev TEXT,
            tund TEXT,
            hind REAL,
            PRIMARY KEY (kuupaev, tund)
        )
    ''')
    conn.commit()
    conn.close()


def save_to_db(df: pd.DataFrame):
    """Save a dataframe to a local database."""
    conn = sqlite3.connect("nordpool_prices.db")
    c = conn.cursor()

    for _, row in df.iterrows():
        c.execute('''
            INSERT OR IGNORE INTO prices (kuupaev, tund, hind)
            VALUES (?, ?, ?)
        ''', (row["Kuupäev"], row["Tund"], row["Hind (€/MWh)"]))

    conn.commit()
    conn.close()


def load_from_db(date: str) -> pd.DataFrame:
    """Load a dataframe from a local database."""
    conn = sqlite3.connect("nordpool_prices.db")
    df = pd.read_sql_query("SELECT * FROM prices WHERE kuupaev = ?", conn, params=(date,))
    conn.close()
    return df


def data_exists(date: str) -> bool:
    """Check if a dataframe exists."""
    return not load_from_db(date).empty


def scraper(date: str):
    """Scrape prices from Nordpool using playwright. Using specific html class to find the data. Returns dataframe."""
    url = f"https://data.nordpoolgroup.com/auction/day-ahead/prices?deliveryDate={date}&currency=EUR&aggregation=DeliveryPeriod&deliveryAreas=EE"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)

        try:
            page.locator("#onetrust-accept-btn-handler").click(timeout=5000)
        except:
            pass

        try:
            page.wait_for_selector("tr.dx-row.dx-data-row.dx-column-lines", timeout=60000)
        except:
            raise (Exception("cant find html class"))

        rows = page.query_selector_all("tr.dx-row.dx-data-row.dx-column-lines")

        tunnid = []
        hinnad = []

        for row in rows:
            tds = row.query_selector_all("td")
            if len(tds) < 2:
                continue

            tund = tds[0].inner_text().strip()
            hind_text = tds[1].inner_text().strip()

            hind = float(hind_text.replace(",", "."))

            tunnid.append(tund)
            hinnad.append(hind)

        browser.close()

    df = pd.DataFrame({
        "Kuupäev": [date] * len(tunnid),
        "Tund": tunnid,
        "Hind (€/MWh)": hinnad
    })

    return df


def get_data(date: str) -> pd.DataFrame:
    """Get data from a local database."""
    init_db()
    if data_exists(date):
        return load_from_db(date)
    else:
        df = scraper(date)
        save_to_db(df)
        return df


def get_daily_avg(date: str) -> float:
    """Get  avg of prices for a specific date."""
    import sqlite3

    conn = sqlite3.connect("nordpool_prices.db")
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(hind) FROM prices WHERE kuupaev = ?", (date,))
    result = cursor.fetchone()[0]

    conn.close()
    return result if result is not None else 0.0

if __name__ == "__main__":
    if len(sys.argv) > 1:
        date = sys.argv[1]
    else:
        date = default = datetime.date.today().isoformat()

    df = get_data(date)
    print(get_daily_avg(date))
