#!/usr/bin/python3

#imported modules---------------------
import os
from pyfiglet import Figlet
from csv import reader
import time 
import random
#-------------------------------------

#Script starts and prints welcome text
custom_txt = Figlet(font="future")

print(custom_txt.renderText("Summoning the Void"))

print("Your Darkest Secrets wii now be banished into the Void")

#------------------------------------

#MAC Add spoofing--------------------

time.sleep(0.2)

# Control flow that checks if the connection is working

hostname = "5.9.95.167"

#The Parameter -c manages in a UNIX System the amount of packets sent
# For Windows this param is -n

response = None

#start of the while loop
while response != 0:
    os.system("ip link set dev eth0 down")

#importing the MAC-vend.csv chosen as random for the first 24Bits.
    lines = open("vendormac.txt").read().splitlines()
    myline = random.choice(lines)
    
    
    mac = myline
    fulladd = None
    for number in range(16**6):
        hex_num = hex(number)[2:].zfill(6)
        fulladd ="{}{}{}:{}{}:{}{}".format(mac,*hex_num)
        break


   # using the randomly chosen vendor octets, generating 3 random octets

#sending the command to the shell
    os.system("ip link set dev address " + fulladd)

#reactivating the NIC
    os.system("ip link set dev  eth0 up")

#checking the functionality of th enew generated address
    response = os.system("ping -c 4 " + hostname) 
    
    if response == 0:   
        print("Connection is working..")
        print("MAC Spoofing was successfull")
        print("Your new MAC Address is "+ fulladd)
        break
    else:
        print("Connection failed...")
        print("Spoofing again") 
# end of the while loop


#end of MAC add spoofing------------------------



time.sleep(1.0)

os.system("sdmem -fllv")

os.system("/etc/init.d/nscd restart")

#os.system("anonsurf start")


print("Insert your new Hostname below:")    
newhost= input("")


os.system("hostname " + newhost)

print("You have a new identity")

print("Your secrets will never see the sunlight again...")

