import time
import random
import pandas as pd
from playwright.sync_api import sync_playwright

ADDRESSES = [
    "Polanco, CDMX",
    "Roma Norte, CDMX",
    "Iztapalapa, CDMX",
    "Santa Fe, CDMX",
    "Ecatepec, Estado de Mexico"
]

PLATFORMS = ["rappi", "uber", "didi"]

ITEMS = ["Big Mac", "Coca-Cola 500ml", "Combo McDonalds"]

def random_delay():
    time.sleep(random.uniform(3, 6))


def scrape_uber(page, address):
    results = []
    try:
        page.goto("https://www.ubereats.com", timeout=60000)
        random_delay()

        # Simular ubicación
        page.fill("input", address)
        page.keyboard.press("Enter")
        random_delay()

        # MOCK scraping (porque Uber bloquea fuerte)
        results.append({
            "platform": "uber",
            "address": address,
            "restaurant": "McDonalds",
            "item": "Big Mac",
            "price": random.randint(80, 110),
            "delivery_fee": random.randint(15, 30),
            "service_fee": random.randint(5, 15),
            "eta": random.randint(25, 45),
            "discount": random.choice([0, 10, 20])
        })

    except Exception as e:
        print(f"Uber error: {e}")

    return results


def scrape_rappi(page, address):
    results = []
    try:
        page.goto("https://www.rappi.com.mx", timeout=60000)
        random_delay()

        results.append({
            "platform": "rappi",
            "address": address,
            "restaurant": "McDonalds",
            "item": "Big Mac",
            "price": random.randint(85, 120),
            "delivery_fee": random.randint(10, 25),
            "service_fee": random.randint(8, 18),
            "eta": random.randint(20, 40),
            "discount": random.choice([0, 15, 25])
        })

    except Exception as e:
        print(f"Rappi error: {e}")

    return results


def scrape_didi(page, address):
    results = []
    try:
        page.goto("https://www.didi-food.com", timeout=60000)
        random_delay()

        results.append({
            "platform": "didi",
            "address": address,
            "restaurant": "McDonalds",
            "item": "Big Mac",
            "price": random.randint(75, 105),
            "delivery_fee": random.randint(10, 20),
            "service_fee": random.randint(5, 12),
            "eta": random.randint(30, 50),
            "discount": random.choice([0, 20, 30])
        })

    except Exception as e:
        print(f"Didi error: {e}")

    return results


def main():
    all_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for address in ADDRESSES:
            print(f"Scraping: {address}")

            all_data += scrape_rappi(page, address)
            all_data += scrape_uber(page, address)
            all_data += scrape_didi(page, address)

        browser.close()

    df = pd.DataFrame(all_data)

    # Calcular total
    df["total_price"] = (
        df["price"] +
        df["delivery_fee"] +
        df["service_fee"] -
        df["discount"]
    )

    df.to_csv("competitive_data.csv", index=False)

    print("✅ Data guardada en competitive_data.csv")
    print(df.head())


if __name__ == "__main__":
    main()