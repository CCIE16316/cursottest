import ipaddress

net = ipaddress.ip_network('192.168.2.0/24')

ip_in_range = ipaddress.ip_address('192.168.2.14') in net 
print(ip_in_range)
# 这里会返回True

