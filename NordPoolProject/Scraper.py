from playwright.sync_api import sync_playwright
import pandas as pd
import re

def scraper(date: str):
    url = f"https://data.nordpoolgroup.com/auction/day-ahead/prices?deliveryDate={date}&currency=EUR&aggregation=DeliveryPeriod&deliveryAreas=EE"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)

        try:
            page.locator("#onetrust-accept-btn-handler").click(timeout=5000)
        except:
            pass

        page.wait_for_selector("tr.dx-row.dx-data-row.dx-column-lines", timeout=60000)

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
        "Date": [date] * len(tunnid),
        "Hour": tunnid,
        "Price (€/MWh)": hinnad
    })


    return df

def calculate_daily_average(df: pd.DataFrame, date: str):
    daily_total = df["Price (€/MWh)"].sum()

    total_row = {"Date": date, "Hour": "Total", "Price (€/MWh)": daily_total}
    df = df._append(total_row, ignore_index=True)
    return df