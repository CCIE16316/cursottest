
from scapy.all import Ether,IP,TCP,sr1
# tcp_pkg = Ether()/IP()/TCP(dport=443)
# tcp_pkg.show()
# 这里就显示TCP报文的详细信息，比如dport就是https

ip_pkt = IP(src="192.168.2.1", dst="192.168.2.34")
tcp_pkt = TCP(sport=80,dport=443)
ip_tcp = Ether()/tcp_pkt/ip_pkt
ip_tcp.show()
# 这里通过变量构建


