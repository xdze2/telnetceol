
from utils import TelnetClient


telnet = TelnetClient("192.168.0.11")

response = telnet.request('NSE')
print(response)

print('\n'.join([line.decode("utf-8").strip() for line in response]))


# AMX
# AMXB<-UUID=00-05-cd-64-45-15><-SDKClass=NetworkPlayer><-Make=Marantz><-Model=RCD-N9><-Revision=11.1.0>

# ZM?
# PWON
# SITUNER