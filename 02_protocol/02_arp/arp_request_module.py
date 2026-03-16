# ARP 请求
# 比如源MAC就是发起方的MAC地址，目标MAC就全F二层广播
# 协议号0x0806
# ARP协议里面，Target Internet Addr：问这个IP的MAC地址
# 答案就是发送者的硬件地址

from scapy.all import ARP,sr1
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

def arp_request_func(ip_address):
    try:
        result_raw = sr1(ARP(pdst=ip_address),
            timeout=1,
            verbose=False
        )
        return ip_address, result_raw.getlayer(ARP).fields.get('hwsrc')
    except AttributeError:
        return ip_address, None

if __name__ == "__main__":
    arp_result = arp_request_func('192.168.2.10')
    print("IP地址：",arp_result[0], "MAC地址：", arp_result[1])
# 0号位就是IP地址，我们输入进去的192.168.2.34,1号位置就是hwsrc 其实就是要请求的MAC地址
