import os
from pyfiglet import Figlet
import time 

#Script starts and prints welcome text
#custom_txt = Figlet(font="future")

#print(custom_txt.renderText("Shieldwall is running"))

# Macaddress is being changed
os.system("ifconfig eth0 down")
os.system("macchanger -A eth0")
os.system("ifconfig eth0 up")

time.sleep(0.2)
# Control flow that checks if the connection is working

hostname = "5.9.95.167"

#The Parameter -c manages in a UNIX System the amount of packets sent
# For Windows this param is -n

response = os.system("ping -c 4 " + hostname) 

if response == 0:   
    print("Connection is working..")
    print("MAC Spoofing was successfull")
else:
    print("Connection failed..")
    print("Spoofing again")
    


