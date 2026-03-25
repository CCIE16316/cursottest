from scapy.all import ICMP,IP,sr1

packet_icmp_echo = IP(dst='192.168.2.34') / ICMP()
result_icmp_echo = sr1(packet_icmp_echo,verbose=False,timeout=1)
print(result_icmp_echo.show())
print('-' * 100)
ip_ver = result_icmp_echo.getlayer("IP").fields["version"]
ip_lengh = result_icmp_echo.getlayer("IP").fields["len"]
ip_ttl = result_icmp_echo.getlayer("IP").fields["ttl"]
ip_proto = result_icmp_echo.getlayer("IP").fields["proto"]
ip_src = result_icmp_echo.getlayer("IP").fields["src"]
ip_dst = result_icmp_echo.getlayer("IP").fields["dst"]
format_head = f"| {'IP Version':<20} | {'IP Length':<20} | {'IP TTL':<20} | {'IP Protocol':<20} | {'IP Address Source':<20} {'IP Address Destination':<20} |"
format_str = f"| {ip_ver:<20} | {ip_lengh:<20} | {ip_ttl:<20} | {ip_proto:<20} | {ip_src:<20} | {ip_dst:<20} |"
print('-'*138)
print(format_head)
print('-'*138)
print(format_str)
print('-'*138)