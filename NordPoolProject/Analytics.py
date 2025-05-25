from matplotlib import pyplot as plt
import pandas as pd
import Scraper

def get_data(date:str ):
    data = Scraper.scraper(date)
    return data

def visualize_24_hour_change(data: pd.DataFrame):
    price = data["Price (€/MWh)"]

    plt.figure(figsize=(10, 6))
    plt.plot(range(len(price)), price, marker='o', linestyle='-', color='blue')

    plt.xlabel("Hour of Day")
    plt.ylabel("Price (€/MWh)")
    plt.title(f"Nord Pool Day Prices on {data['Date'][0]}")

    tick_positions = range(0, len(price), 2)
    start_hours = data["Hour"].str.split(" - ").str[0]
    tick_labels = [start_hours[i] for i in tick_positions]
    plt.xticks(tick_positions, tick_labels, rotation=45)

    plt.grid(True)
    plt.fill_between(range(len(price)), price, color='blue', alpha=0.4)
    plt.tight_layout()
    plt.savefig('foo.png', bbox_inches='tight')
    plt.show()

def visualize_24_hour_change_between_hours(data: pd.DataFrame):
    price = data["Price (€/MWh)"].values
    data.sort_values("Hour", inplace=True)
    hour_str = data["Hour"].str.split(" - ").str[0]
    hour = hour_str.str.split(":").str[0].astype(int)

    result = [0]
    for i in range(1, len(price)):
        result.append(price[i] - price[i - 1])
    print(hour)
    print(result)
    plt.figure(figsize=(10, 6))
    plt.bar(hour, result, color='orange')
    plt.xlabel("Hour of Day")
    plt.ylabel("Price Change (€/MWh)")
    plt.title(f"Hourly Price Change on {data['Date'][0]}")
    plt.xticks(range(0, 24))
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('foo.png', bbox_inches='tight')
    plt.show()

data = get_data("2025-05-25")
visualize_24_hour_change(data)
visualize_24_hour_change_between_hours(data)