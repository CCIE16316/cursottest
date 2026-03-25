from scapy.all import Ether, IP, TCP,sr1,ICMP,ARP
import re

icmp_echo = IP(dst='192.168.2.34') / ICMP()
ping_result = sr1(icmp_echo, verbose=False, timeout=1) 
# verbose不显示详细信息，timeout=1 超时1秒就停止
# print(ping_result.show())
print('-' * 100)
# print(ping_result.getlayer(IP).fields)
icmp_version = ping_result.getlayer("IP").fields["version"]
icmp_length = ping_result.getlayer("IP").fields["len"]
icmp_proto = ping_result.getlayer("IP").fields["proto"]
icmp_src = ping_result.getlayer("IP").fields["src"]
icmp_dst = ping_result.getlayer("IP").fields["dst"]
header_format = f"| {'ICMP Version':<20} | {'Length':<20} | {'Protocol':<20} | {'Source IP':<20} | {'Destination IP':<20} |"
str_format = f"| {icmp_version:<20} | {icmp_length:<20} | {icmp_proto:<20} | {icmp_src:<20} | {icmp_dst:<20} |"
print('-' * 116)
print(header_format)
print('-' * 116)
print(str_format)
print('-' * 116)