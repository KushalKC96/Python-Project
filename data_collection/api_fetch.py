import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

NEPAL_CITIES = {
    "Kathmandu":  {"lat": 27.7172, "lon": 85.3240},
    "Pokhara":    {"lat": 28.2096, "lon": 83.9856},
    "Biratnagar": {"lat": 26.4525, "lon": 87.2718},
    "Birgunj":    {"lat": 27.0104, "lon": 84.8777},
    "Bharatpur":  {"lat": 27.6833, "lon": 84.4333},
    "Janakpur":   {"lat": 26.7288, "lon": 85.9250},
    "Dharan":     {"lat": 26.8120, "lon": 87.2839},
    "Dhangadhi":  {"lat": 28.6833, "lon": 80.6000},
    "Butwal":     {"lat": 27.7000, "lon": 83.4500},
    "Nepalgunj":  {"lat": 28.0500, "lon": 81.6167},
}

WEATHER_CODES = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Icy fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    80: "Slight showers", 81: "Moderate showers", 82: "Violent showers",
    95: "Thunderstorm", 96: "Thunderstorm with hail",
}

def fetch_historical_weather():
    start_date = "2025-09-01"   # 6 months of historical data
    end_date   = "2026-03-11"   # yesterday (archive API needs 1 day buffer)
    all_data   = []

    print(f"📅 Fetching data: {start_date} to {end_date}\n")

    for city, coords in NEPAL_CITIES.items():
        url = (
            f"https://archive-api.open-meteo.com/v1/archive"
            f"?latitude={coords['lat']}&longitude={coords['lon']}"
            f"&start_date={start_date}&end_date={end_date}"
            f"&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,"
            f"precipitation_sum,windspeed_10m_max,weathercode"
            f"&timezone=Asia/Kathmandu"
        )

        response = requests.get(url)

        if response.status_code == 200:
            data   = response.json()
            daily  = data["daily"]

            for i in range(len(daily["time"])):
                code = daily["weathercode"][i]
                all_data.append({
                    "city":             city,
                    "date":             daily["time"][i],
                    "temp_max_c":       daily["temperature_2m_max"][i],
                    "temp_min_c":       daily["temperature_2m_min"][i],
                    "temperature":      daily["temperature_2m_mean"][i],
                    "precipitation_mm": daily["precipitation_sum"][i],
                    "wind_speed_max":   daily["windspeed_10m_max"][i],
                    "condition":        WEATHER_CODES.get(code, "Unknown"),
                    "source":           "Open-Meteo_API"
                })
            print(f"  ✅ {city}: {len(daily['time'])} days fetched")
        else:
            print(f"  ⚠️ Failed for {city}: {response.status_code}")

    df = pd.DataFrame(all_data)
    print(f"\n📊 Total API records: {len(df)}")
    return df

if __name__ == "__main__":
    df = fetch_historical_weather()
    print(df)