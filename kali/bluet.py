from bluetooth import *

devList = discover_devices()

for device in devList:
  name = str(lookup_name(device))
  print "[+] Found Bluetooth Device " + str(name)
  print "[+] MAC address: "+str(device)
