import ipaddress

net = ipaddress.ip_network('192.168.2.0/24')

for ip in net:
    print(ip)