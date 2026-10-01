import sqlite3

#---Store fetched data in database---
def store_data(df):
    conn = sqlite3.connect("pipeline.db")
    cursor = conn.cursor()

    #---Create table---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            time TEXT UNIQUE,
            temperature_2m REAL
        )
    """)
    conn.commit()

    #---Insert values from DF---
    df_to_insert = df.copy()
    df_to_insert["time"] = df_to_insert["time"].astype(str)

    rows = list(df_to_insert.itertuples(index=False, name=None))
    cursor.executemany("INSERT OR IGNORE INTO weather VALUES (?, ?)", rows)
    conn.commit()
    conn.close()

#---Store summary in database---

from datetime import datetime

def store_summary(summary_text):
    conn = sqlite3.connect("pipeline.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS summaries (
            time TEXT,
            summary_text TEXT
        )
    """)
    conn.commit()

    cursor.execute(
        "INSERT INTO summaries VALUES (?, ?)",
        (datetime.now().isoformat(), summary_text)
    )
    conn.commit()
    conn.close()