import requests
import random

class WhaleTracker:

    def __init__(self):
        self.last_price = None

    async def scan(self):

        signals = []

        try:
            r = requests.get(
                "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
            )

            price = float(r.json()["price"])

            if self.last_price:

                change = (price - self.last_price) / self.last_price

                # momentum long
                if change > 0.002:
                    signals.append({
                        "side": "long",
                        "confidence": 0.85,
                        "symbol": "BTC/USDT"
                    })

                # momentum short
                if change < -0.002:
                    signals.append({
                        "side": "short",
                        "confidence": 0.85,
                        "symbol": "BTC/USDT"
                    })

            self.last_price = price

        except:
            pass

        return signals