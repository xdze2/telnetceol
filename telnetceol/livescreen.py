from datetime import datetime

import rich
from rich.align import Align

from textual.app import App
from textual.widget import Widget


from telnetceol.utils import TelnetClient

telnet_client = TelnetClient('192.168.0.11')

def get_screen():
    response = telnet_client.request("NSE")
    return response


class Clock(Widget):
    def on_mount(self):
        self.set_interval(1, self.refresh)

    def render(self):
        # time = datetime.now().strftime("%c")
        response = [line.decode("utf-8").strip()[4:] for line in get_screen()]
        tx = rich.text.Text('\n'.join(response)) 
        return Align.center(tx, vertical="middle")


class ClockApp(App):
    async def on_mount(self):
        await self.view.dock(Clock())


