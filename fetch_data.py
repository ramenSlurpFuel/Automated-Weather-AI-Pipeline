import requests

response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 40.71, "longitude": -74.01, "hourly": "temperature_2m"}
)

data = response.json()

#------------------------------------------------------------------------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature_2m": data["hourly"]["temperature_2m"],
})

df["time"] = pd.to_datetime(df["time"])

print(df.head())  