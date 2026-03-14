# 之前叫kamene
# 发送、捕获、分析、构造网络数据包

from scapy.all import Ether, IP, TCP

tcp_packet = Ether() / IP() / TCP()
tcp_packet.show()