import telnetlib


def telnet_request(telnet, command, all_lines=False):
    """Execute `command` and return the response."""
    print("Sending: %s" % command)
    telnet.write(command.encode("ASCII") + b"\r")
    lines = []
    while True:
        line = telnet.read_until(b"\r", timeout=0.2)
        if not line:
            break
        lines.append(line)#.decode("ASCII").strip())
        print("Received: %s" % line)

    if all_lines:
        return lines
    return lines[0] if lines else ""


def telnet_command(command):
    """Establish a telnet connection and sends `command`."""
    telnet = telnetlib.Telnet(HOST, 23)
    print("Sending: %s" % command)
    telnet.write(command.encode("ASCII") + b"\r")
    telnet.read_very_eager()  # skip response
    telnet.close()


# telnet_command('PWSTANDBY')
# telnet_command('PWON')

# telnet_command('MUOFF') 
# telnet_command('MUON')


import time

time.sleep(1)
HOST = "192.168.0.11"
telnet = telnetlib.Telnet(HOST, 23)

# _pwstate = telnet_request(telnet, "PW?")
# print(_pwstate)
# time.sleep(1)
# time.sleep(1)
for line in telnet_request(telnet, "MV?", all_lines=True):
    print(line)

# for line in telnet_request(telnet, "SI?", all_lines=True):
#     print(line)

# for line in telnet_request(telnet, "CLK", all_lines=True):
#     print(line)

# # for line in telnet_request(telnet, "TS?", all_lines=True):
# #     print(line)

# # for line in telnet_request(telnet, "TS?", all_lines=True):
# #     print(line)

# # for line in telnet_request(telnet, "TFAN?", all_lines=True):
# #     print(line)

# # for line in telnet_request(telnet, "FV 01", all_lines=True):
# #     print(line)

# for line in telnet_request(telnet, "FV ?", all_lines=True):
#     print(line)

# for line in telnet_request(telnet, "NSA", all_lines=True):
#     print(line)

# # for line in telnet_request(telnet, "NSE", all_lines=True):
# #     print(line)

# for line in telnet_request(telnet, "SIFM", all_lines=True):
#     print(line)

# for line in telnet_request(telnet, "NSA", all_lines=True):
#     print(line)

# telnet.close()
