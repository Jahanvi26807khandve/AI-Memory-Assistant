
import os
from dotenv import load_dotenv
from google import genai

# Load API keys from the .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Ask Gemini a simple question
response = client.models.generate_content(
   model="gemini-3.6-flash",
    contents="Explain Python in one simple sentence."
)

print("Gemini's response:")
print(response.text)
