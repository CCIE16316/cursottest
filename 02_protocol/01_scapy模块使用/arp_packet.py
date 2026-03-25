from scapy.all import Ether,IP,ARP,sr1


arp_request = ARP(pdst='192.168.2.34')
arp_request.show()
result = sr1(arp_request)
print(result.show())
# who-has就是request问谁有这个IP的mac地址
# is-at就是是在，单播回复