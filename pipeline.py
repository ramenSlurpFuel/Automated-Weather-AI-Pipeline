from fetch_data import get_weather_data
from database import store_data

def run_pipeline():
    df = get_weather_data()
    store_data(df)

if __name__ == "__main__":
    run_pipeline()