import requests

response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 40.71, "longitude": -74.01, "hourly": "temperature_2m"}
)
data = response.json()

#---Create DataFrame---
import pandas as pd

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature_2m": data["hourly"]["temperature_2m"],
})

df["time"] = pd.to_datetime(df["time"])

#---Clean Data---
def clean_data(df):
    #---Handle NAs---
    df["temperature_2m"] = df["temperature_2m"].interpolate()

    #---Handle Duplicates---
    df = df.drop_duplicates(subset="time")

    #---Handle Order---
    if not df["time"].is_monotonic_increasing:
        df = df.sort_values("time").reset_index(drop=True)

    return df

df = clean_data(df)