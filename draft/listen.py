
#!/usr/bin/python


from utils import TelnetClient, format_response


telnet = TelnetClient("192.168.0.11")

telnet.listen()
