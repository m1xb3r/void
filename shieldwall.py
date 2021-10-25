import os
from pyfiglet import Figlet
import time 

#Script starts and prints welcome text
custom_txt = Figlet(font="future")

print(custom_txt.renderText("Shieldwall is running"))

# Macaddress is being changed
os.system("ifconfig eth0 down")
os.system("macchanger -A eth0")
os.system("ifconfig eth0 up")

time.sleep(0.2)
# Control flow that checks if the connection is working
to_ping = ["google.com"]

for ip in to_ping:
    response = os.popen(f"ping {ip}").read()
    if "Received = 1" in response:
        print(f"MAC spoofing was successfull")
    else:
        print(f"No connection, MAC spoofing restarts")
