import telnetlib
from typing import List


class TelnetClient:
    def __init__(self, host_ip: str):
        self.telnet = telnetlib.Telnet(host_ip, 23)

    def request(self, command: str, verbose: bool = False):
        """Execute `command` and return the response."""
        if verbose: print("Sending: %s" % command)
        self.telnet.write(command.encode("ASCII") + b"\r")
        lines = []
        while True:
            line = self.telnet.read_until(b"\r", timeout=0.2)
            if not line:
                break
            lines.append(line)

        return lines

    def listen(self):
        while True:
            line = self.telnet.read_until(b"\r", timeout=1.0)
            print(line)


def format_response(response: List[bytes]) -> str:
    return '\n'.join([line.decode("utf-8").strip() for line in response])