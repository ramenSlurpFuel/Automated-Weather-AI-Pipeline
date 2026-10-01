from fetch_data import get_weather_data
from database import store_data
from summarise import generate_summary

def run_pipeline():
    print("fetching...")
    df = get_weather_data()
    print("fetched, storing...")
    store_data(df)
    print("stored, summarizing...")
    summary = generate_summary(df)
    print("done")
    print(summary)

if __name__ == "__main__":
    run_pipeline()