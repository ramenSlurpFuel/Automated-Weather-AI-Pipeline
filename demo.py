print("Hello World")

from dotenv import load_dotenv
import os
load_dotenv()  # reads .env and loads variables into the environment

api_key = os.getenv("ANTHROPIC_API_KEY")

print(f"ANTHROPIC_API_KEY: {api_key}")