import time
from pipeline import run_pipeline

INTERVAL_SECONDS = 3600

while True:
    try:
        run_pipeline()
    except Exception as e:
        print(f"Pipeline run failed: {e}")

    time.sleep(INTERVAL_SECONDS)