import ipaddress

net1 = ipaddress.ip_network('192.168.2.0/24')

def sort_ip(net1):
    return sorted(net1, key=lambda ip: ipaddress.ip_address(ip))