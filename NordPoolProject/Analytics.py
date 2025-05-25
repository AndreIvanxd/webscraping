from matplotlib import pyplot as plt
import pandas as pd
import Scraper
import sys
import datetime


def get_data(date:str ):
    data = Scraper.scraper(date)
    return data

def visualize_24_hour_chart(data: pd.DataFrame):
    price = data["Hind (€/MWh)"]

    plt.figure(figsize=(10, 6))
    plt.plot(range(len(price)), price, marker='o', linestyle='-', color='blue')

    plt.xlabel("Tund")
    plt.ylabel("Hind (€/MWh)")
    plt.title(f"Nord Pool päeva hind {data['Kuupäev'][0]}")

    tick_positions = range(0, len(price), 2)
    start_hours = data["Tund"].str.split(" - ").str[0]
    tick_labels = [start_hours[i] for i in tick_positions]
    plt.xticks(tick_positions, tick_labels, rotation=45)
    plt.grid(True)
    plt.fill_between(range(len(price)), price, color='blue', alpha=0.4)
    plt.tight_layout()
    plt.savefig(f'graafid/24_hour_chart{data["Kuupäev"][0]}.png', bbox_inches='tight')
    plt.show()
def visualize_24_hour_change_between_hours(data: pd.DataFrame):
    price = data["Hind (€/MWh)"].values
    data.sort_values("Tund", inplace=True)
    hour_str = data["Tund"].str.split(" - ").str[0]
    hour = hour_str.str.split(":").str[0].astype(int)

    result = [0]
    for i in range(1, len(price)):
        result.append(price[i] - price[i - 1])

    plt.figure(figsize=(10, 6))
    plt.bar(hour, result, color='orange')
    plt.xlabel("Tund")
    plt.ylabel("Hinna muutus (€/MWh)")
    plt.title(f"Iga tunnine hinna muutus {data['Kuupäev'][0]}")
    plt.xticks(range(0, 24))
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig(f'graafid/change_between_hours{data["Kuupäev"][0]}.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        date = sys.argv[1]
    else:
        date = default=datetime.date.today().isoformat()

    data = get_data(date)
    visualize_24_hour_change_between_hours(data)
    visualize_24_hour_chart(data)