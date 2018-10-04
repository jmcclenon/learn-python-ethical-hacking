#!/usr/local/bin/python

import subprocess

interface = 'enp0s3'
new_mac = "00:11:22:33:44:77"
old_mac = "08:00:27:a5:66:83"

print(interface)
print(new_mac)
print(old_mac)



print("[+] Changing MAC address for " + interface)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether" + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
