from scapy.all import *

def findVnts(pkt):
  raw = pkt.sprintf('%Raw.load%')
  reUser = re.findall('vnt[a-z]{3,4}', raw)
  if reUser:
    print 'Found: ' + reUser[0]
    print raw

conf.iface = 'wlp2s0' #'mon0'
sniff(prn=findVnts, store=0)

