import ipaddress

ip_list = ['172.16.12.123','10.1.1.34','172.16.12.3','172.16.12.234','172.16.12.12','192.168.1.123','172.16.12.23']

result = sorted(ip_list, key=lambda ip: ipaddress.ip_address(ip)) # 把他变成ip_address对象
print(result)