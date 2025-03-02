import os
from dotenv import load_dotenv

# Load environment variables from a .env file located in the same directory
load_dotenv()

# Retrieve the API key from the environment variables
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("Missing API_KEY in environment variables. Please set it in your .env file.")

# Retrieve the model setting with a default value if not set
MODEL = os.getenv("MODEL", "gpt-4o-mini")


print(MODEL)