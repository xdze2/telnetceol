import time
from rich.live import Live
from rich import print
from rich.panel import Panel


class LiveScreen:
    def __init__(self, telnet_client=None):
        self.telnet_client = telnet_client

    def run(self):
        with Live(refresh_per_second=4) as live:
            while True:
                time.sleep(0.4)  # arbitrary delay
                live.update(self.render())

    def render(self):
        raw_response = self.telnet_client.request("NSE")
        response = [line.decode("utf-8").strip()[4:] for line in raw_response if line]
        tx = Panel("\n".join(response), title="Denon Ceol", width=50, height=9 + 2)
        return tx
