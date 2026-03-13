import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_nepal_weather():
    url = "https://www.weather-forecast.com/countries/Nepal"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    scraped_data = []
    city_items = soup.select("ul li a[href*='/locations/']")

    for item in city_items:
        city_name = item.get_text(strip=True)
        parent = item.find_parent("li")
        img_tag = parent.find("img")
        condition = img_tag["alt"] if img_tag else "N/A"

        if " and " in condition:
            condition_clean = condition.split(" and ")[0]
            temp_str = condition.split(" and ")[1].split("°")[0]
            try:
                temp_value = float(temp_str)
            except:
                temp_value = None
        else:
            condition_clean = condition
            temp_value = None

        scraped_data.append({
            "city":             city_name,
            "date":             datetime.today().strftime("%Y-%m-%d"),
            "temp_max_c":       None,   # not available from scraper
            "temp_min_c":       None,   # not available from scraper
            "temperature":      temp_value,
            "precipitation_mm": None,   # not available from scraper
            "wind_speed_max":   None,   # not available from scraper
            "condition":        condition_clean,
            "source":           "BeautifulSoup"
        })

    df = pd.DataFrame(scraped_data)
    print(f"✅ Scraped {len(df)} cities via BeautifulSoup")
    return df

if __name__ == "__main__":
    df = scrape_nepal_weather()
    print(df)