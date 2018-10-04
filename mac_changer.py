#/usr/bin/env python
# by John McClenon, Jr
# With a little help from my friends

import subprocess

interface = eth0
new_mac = "00:11:22:33:44:77"

print("[+] Changing MAC address for " + interface

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether" + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
