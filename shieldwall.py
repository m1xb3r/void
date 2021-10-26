import os
from pyfiglet import Figlet
import time 

#Script starts and prints welcome text
custom_txt = Figlet(font="future")

print(custom_txt.renderText("Summoning the Void"))

print("Your Darkest Secrets wii now be banished into the Void")

# MAC Add spoofing

time.sleep(0.2)
# Control flow that checks if the connection is working

hostname = "5.9.95.167"

#The Parameter -c manages in a UNIX System the amount of packets sent
# For Windows this param is -n

response = os.system("ping -c 4 " + hostname) 

while response != 0:
    
    os.sytem("ifconfig eth0 down")
    os.system("macchanger -A eth0")
    os.system("ifconfig eth0 up")
    if response == 0:   
        print("Connection is working..")
        print("MAC Spoofing was successfull")
        break
    else:
        print("Connection failed..")
        print("Spoofing again") 

print("Insert your new Hostname below:")    
newhost= input("")

os.system("hostname " + newhost)

print("You have a new identity")


time.sleep(1.0)

os.system("sdmem -fllv")

os.system("/etc/init.d/nscd restart")

os.system("anonsurf start")

print("Your secrets will never see the sunlight again...")

