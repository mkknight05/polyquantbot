import asyncio
import yaml

from whale_tracker import WhaleTracker
from futures_engine import FuturesEngine
from arbitrage_engine import ArbitrageEngine
from reporter import Reporter

with open("config.yaml") as f:
    config = yaml.safe_load(f)

mode = config["mode"]
sim_cycles = config["simulation"]["duration_cycles"]

async def main():

    whale = WhaleTracker()
    futures = FuturesEngine()
    arb = ArbitrageEngine()
    report = Reporter()

    cycles = 0
    live = False

    while True:

        cycles += 1

        if cycles >= sim_cycles:
            live = True

        signals = await whale.scan()

        for s in signals:
            await futures.execute_signal(s, live)

        await arb.scan()
        await report.update(live)

        await asyncio.sleep(2)

asyncio.run(main())