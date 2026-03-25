from scapy.all import ARP,sr1

def arp_requst_fun(pdst_ip_address):
    result_raw = sr1(ARP(pdst=pdst_ip_address),verbose=False,timeout=1)
    return pdst_ip_address, result_raw.getlayer(ARP).fields['hwsrc']

result = arp_requst_fun("192.168.2.34")
print(f"Request Destination IP is {result[0]}, Request Destination MAC Address is {result[1]}")