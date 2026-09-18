import sqlite3
import pandas as pd

#---Fetch Data from SQLite Database---
conn = sqlite3.connect("pipeline.db")
df = pd.read_sql_query("SELECT * FROM weather", conn)
conn.close()

#---Convert time column to datetime and extract hour and day of year---
df["time"] = pd.to_datetime(df["time"])

df["hour"] = df["time"].dt.hour
df["day_of_year"] = df["time"].dt.dayofyear

#---Separate DF, Create train/test splits---
X = df[["hour", "day_of_year"]]
y = df["temperature_2m"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#---Training---
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

#---Evaluation---
from sklearn.metrics import mean_absolute_error, r2_score

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.2f}")

#---Save Model---
import joblib

joblib.dump(model, "model.pkl")