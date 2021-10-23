
from utils import TelnetClient

import time
from itertools import combinations_with_replacement

telnet = TelnetClient("192.168.0.11")

reponse = telnet.request('SI?')
print(reponse)


alphabet = "AZERTYUIOPQSDFGHJKLMWXCVBN"

print('scan -')
for cmd in combinations_with_replacement(alphabet, 3):
    cmd = ''.join(cmd)
    reponse = telnet.request(cmd)
    print(cmd, end='\r')
    if reponse:
        print('\n')
        print(cmd, reponse)
