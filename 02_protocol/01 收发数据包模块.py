# # 之前叫kamene
# # 发送、捕获、分析、构造网络数据包
from tabnanny import verbose
from scapy.all import Ether, IP, TCP,sr1,ICMP,ARP

# # 1.1 构造一个TCP报文1
# tcp_packet = Ether() / IP() / TCP(dport=443)
# tcp_packet.show()
# # show()，显示报文详细


# # 1.2 构造一个TCP报文2
# ip_packet = IP(src="192.168.2.38", dst="192.168.2.34")
# tcp_packet = TCP(dport=443)
# ip_tcp = Ether() / ip_packet / tcp_packet
# ip_tcp.show()
# # 可以单独修改


# # 1.3 发送、接收1个TCP报文
# sr1(ip_tcp)
# # 发送1个报文,接收1个报文

# # 1.4 构造一个ICMP报文
# icmp_echo = IP(dst='192.168.2.34') / ICMP()
# ping_result = sr1(icmp_echo)
# print(ping_result.show())
# # 查看ICMP响应报文详细
# # 这里都建议使用sr1函数，发一个回1个的。


# # 1.5 构造一个ARP报文
# arp_request = ARP(pdst='192.168.2.34')
# arp_request.show()
# result = sr1(arp_request)
# print(result.show())
# # 查看接收响应报文

# 1.6 构造一个ICMP报文
icmp_echo1 = IP(dst='192.168.2.34') / ICMP()
ping_result1 = sr1(icmp_echo1, verbose=False, timeout=1) # verbose不显示详细信息，timeout=1 超时1秒就停止
print(ping_result1.show())
# 查看ICMP响应报文详细
# 这里都建议使用sr1函数，发一个回1个的。