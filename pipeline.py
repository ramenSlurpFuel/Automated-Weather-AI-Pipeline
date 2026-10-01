from fetch_data import get_weather_data
from database import store_data, store_summary
from summarise import generate_summary

def run_pipeline():
    df = get_weather_data()
    store_data(df)
    summary = generate_summary(df)
    store_summary(summary)

if __name__ == "__main__":
    run_pipeline()