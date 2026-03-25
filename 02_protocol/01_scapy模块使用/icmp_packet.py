from scapy.all import ICMP,IP,sr1


packet_ip = IP(src='192.168.2.36', dst='192.168.2.34')
# packet_ip.show()
icmp_echo = packet_ip / ICMP()
result = sr1(icmp_echo, verbose=False, timeout=1)
# verbose不显示详细信息，timeout=1 超时1秒就停止
print(result.show())