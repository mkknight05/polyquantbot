import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

print("KEY:", repr(os.getenv("OKX_API_KEY")))
print("SECRET:", repr(os.getenv("OKX_SECRET")))
print("PASS:", repr(os.getenv("OKX_PASSPHRASE")))

try:
    exchange = ccxt.okx({
        "apiKey": os.getenv("OKX_API_KEY"),
        "secret": os.getenv("OKX_SECRET"),
        "password": os.getenv("OKX_PASSPHRASE"),
        "headers": {
            "x-simulated-trading": "1"
        }
    })

    balance = exchange.fetch_balance()
    print("✅ OKX Connected")
    print(balance["total"])

except Exception as e:
    print("❌ OKX Connection Failed")
    print(e)