from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
API_KEY = os.getenv("API_KEY")

client = genai.Client(api_key=API_KEY)

def generate_summary(df):
    prompt = f"""
Here is recent weather data (time and temperature in Celsius):

{df.to_string(index=False)}

Write a 2 sentence plain english summary of this data for a dashboard.
"""

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return interaction.output_text