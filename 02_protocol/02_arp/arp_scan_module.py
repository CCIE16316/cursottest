import ipaddress
from multiprocessing.pool import ThreadPool
import sys
from pathlib import Path

current_file = Path(__file__)
project_root = current_file.parent.parent
sys.path.append(str(project_root))

from arp_request_module import arp_request_func

def scapy_arp_scan_func(network):
    net = ipaddress.ip_network(network)
    ip_list = [ str(ip_add) for ip_add in net]
    pool = ThreadPool(processes=100)
    result = [pool.apply_async(arp_request_func, args=(i,)) for i in ip_list]
    pool.close()
    pool.join()
    scan_dict = {}
    for r in result:
        if r.get()[1]:
            scan_dict[r.get()[0]] = r.get()[1]
    return scan_dict


if __name__ == '__main__':
    for ip, mac in scapy_arp_scan_func("192.168.2.0/24").items():
        print("IP地址："+ip+'是活动的，他的MAC地址是：'+mac)



