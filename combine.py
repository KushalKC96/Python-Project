import pandas as pd
from scraper import scrape_nepal_weather
from api_fetch import fetch_historical_weather

def combine_and_save():
    print("=" * 50)
    print("🔄 Step 1: BeautifulSoup Scraping...")
    print("=" * 50)
    df_scraped = scrape_nepal_weather()

    print("\n" + "=" * 50)
    print("🔄 Step 2: Open-Meteo API Fetch (March 1-7)...")
    print("=" * 50)
    df_api = fetch_historical_weather()

    print("\n" + "=" * 50)
    print("🔄 Step 3: Combining...")
    print("=" * 50)
    df_combined = pd.concat([df_scraped, df_api], ignore_index=True)

    # Save CSV
    df_combined.to_csv("nepal_weather_data.csv", index=False)

    print(f"\n✅ CSV saved: nepal_weather_data.csv")
    print(f"📊 Total records : {len(df_combined)}")
    print(f"   - BeautifulSoup: {len(df_scraped)} rows")
    print(f"   - API          : {len(df_api)} rows")
    print("\n", df_combined.head(10))

if __name__ == "__main__":
    combine_and_save()