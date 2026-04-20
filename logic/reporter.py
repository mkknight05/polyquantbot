class Reporter:

    def __init__(self):
        self.cycles = 0

    async def update(self, live):

        self.cycles += 1

        mode = "LIVE" if live else "SIM"

        print(f"[{mode}] cycle {self.cycles}")