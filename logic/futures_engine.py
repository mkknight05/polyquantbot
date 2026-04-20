import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

class FuturesEngine:

    def __init__(self):

        self.exchange = ccxt.okx({
            "apiKey": os.getenv("OKX_API_KEY"),
            "secret": os.getenv("OKX_SECRET"),
            "password": os.getenv("OKX_PASSPHRASE"),
        })

    async def execute_signal(self, signal, live):

        if signal["confidence"] < 0.8:
            return

        side = "buy" if signal["side"] == "long" else "sell"

        symbol = "BTC/USDT:USDT"
        size = 0.001

        if not live:
            print("SIM OKX TRADE", side)
            return

        try:
            print("LIVE OKX TRADE", side)

            # enable later
            # self.exchange.create_market_order(symbol, side, size)

        except Exception as e:
            print("OKX error:", e)