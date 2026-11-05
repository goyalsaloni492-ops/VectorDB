from dotenv import load_dotenv
import os

load_dotenv()

print("SARVAM =", os.getenv("SARVAM_API_KEY"))
print("MISTRAL =", os.getenv("MISTRAL_API_KEY"))