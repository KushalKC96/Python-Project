import pandas as pd
from data_collection.scraper import scrape_nepal_weather
from data_collection.api_fetch import fetch_historical_weather

# Consistent column order across both sources
COLUMNS = [
    "city", "date",
    "temp_max_c", "temp_min_c", "temperature",
    "precipitation_mm", "wind_speed_max",
    "condition", "source"
]

def combine_and_save():
    print("=" * 50)
    print("🔄 Step 1: BeautifulSoup Scraping (today)...")
    print("=" * 50)
    df_scraped = scrape_nepal_weather()

    print("\n" + "=" * 50)
    print("🔄 Step 2: Open-Meteo API Fetch (Sep 2025 - Mar 2026)...")
    print("=" * 50)
    df_api = fetch_historical_weather()

    print("\n" + "=" * 50)
    print("🔄 Step 3: Combining...")
    print("=" * 50)

    # Enforce same column order on both before concat
    df_scraped = df_scraped.reindex(columns=COLUMNS)
    df_api     = df_api.reindex(columns=COLUMNS)

    df_combined = pd.concat([df_scraped, df_api], ignore_index=True)

    # Sort by city then date
    df_combined["date"] = pd.to_datetime(df_combined["date"])
    df_combined = df_combined.sort_values(["city", "date"]).reset_index(drop=True)

    # Save CSV
    df_combined.to_csv("nepal_weather_data.csv", index=False)

    print(f"\n✅ CSV saved: nepal_weather_data.csv")
    print(f"📊 Total records : {len(df_combined)}")
    print(f"   - BeautifulSoup : {len(df_scraped)} rows (today's live data)")
    print(f"   - Open-Meteo API: {len(df_api)} rows  (6 months historical)")
    print(f"\nColumns: {list(df_combined.columns)}")
    print(f"\nMissing values:\n{df_combined.isnull().sum()}")
    print("\nSample:\n", df_combined.head(10))

if __name__ == "__main__":
    combine_and_save()