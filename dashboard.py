import streamlit as st
import sqlite3
import pandas as pd

st.title("Weather Pipeline Dashboard")

conn = sqlite3.connect("pipeline.db")

df = pd.read_sql_query("SELECT * FROM weather", conn)
summary_df = pd.read_sql_query(
    "SELECT * FROM summaries ORDER BY time DESC LIMIT 1", conn
)

conn.close()

df["time"] = pd.to_datetime(df["time"])
df = df.set_index("time")

st.line_chart(df["temperature_2m"])

st.subheader("Latest Forecast Summary")
if not summary_df.empty:
    st.write(summary_df["summary_text"].iloc[0])