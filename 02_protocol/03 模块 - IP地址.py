import ipaddress

net1 = ipaddress.ip_network('192.168.2.0/24')
for ip in net1:
    print (str(ip))
    # print(type(ip))
    # 这里的ip不是字符串，是Class，所以要转换成字符串。
print(net1.num_addresses)
# 统计数量
print(ipaddress.ip_address('192.168.2.2') in net1)
# 判断地址是否在范围内


# 1.1 IP排序

def sort_ip(net1):
    return sorted(net1, key=lambda ip: ipaddress.ip_address(ip))