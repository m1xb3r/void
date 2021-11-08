#!/usr/bin/env python3

#imported modules---------------------
from os.path import basename, isfile
import os
from subprocess import call, check_call, CalledProcessError, getoutput, Popen
from sys import exit, stdout, stderr
from time import sleep
import random
#-------------------------------------
#Script starts and prints welcome text
print("Summoning the Void")
print("Your Darkest Secrets wii now be banished into the Void")
#------------------------------------
#MAC Add spoofing-------------------
# Control flow that checks if the connection is working
hostname = "1.1.1.1"
#The Parameter -c manages in a UNIX System the amount of packets sent
# For Windows this param is -n
response = None
#start of the while loop-------------------------------------------------------
while response != 0:
    Popen("ip link set dev eth0 down", shell= True )
#importing the vendormac.txt chosen as random for the first 24Bits.
    lines = open("vendormac.txt").read().splitlines()
    myline = random.choice(lines)

    mac = myline
    fulladd = None
    fulladd = mac+"%02x:%02x:%02x" % (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))
   # using the randomly chosen vendor octets, generating 3 random octets
#Adding blacklist check
    with open("blacklist.txt", "r") as blacklist:
        if fulladd in blacklist.read():
            print("Address is already blacklisted")
            continue

    Popen("ip link set dev address " + fulladd, shell= True )
    Popen("ip link set dev  eth0 up", shell= True )
    response = os.system("ping -c 4 " + hostname)

    if response == 0:
        print("Connection is working..")
        print("MAC Spoofing was successfull")
        print("Your new MAC Address is "+ fulladd)
        break
    else:
        print("Connection failed...")
        print("Blacklisting MAC Address")
        with open("blacklist.txt", "a") as blacklist:
            blacklist.write(fulladd+ "\n")
        print("Spoofing again")
# end of the while loop
#end of MAC add spoofing-------------------------------------------------------
sleep(1.0)
print("Insert your new Hostname below:")
newhost= input("")
Popen("hostname " + newhost, shell= True)
print("You have a new identity")
os.system("sdmem -fllv")
#call("anonsurf start")
# TOR routing start----------------------------
print(newhost)

# TOR routing end----------------------------
print("Your secrets will never see the sunlight again...")
