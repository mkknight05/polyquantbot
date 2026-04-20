import os
from dotenv import load_dotenv

load_dotenv()

print("API KEY:", os.getenv("COINBASE_API_KEY"))
print("KEY FILE:", os.getenv("COINBASE_KEY_FILE"))

try:
    with open(os.getenv("COINBASE_KEY_FILE")) as f:
        key = f.read()
    print("✅ Coinbase key file loaded")
except Exception as e:
    print("❌ Coinbase key load failed")
    print(e)