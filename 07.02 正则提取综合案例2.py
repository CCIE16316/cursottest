import re


display_ip_interface_brief_line = "Vlanif20        20.1.1.254/24    up     up"
ipv4_basic = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d+"
# 这里的/就是斜杠
# ipv4_basic = r"(?:\d{1,3}\.){3}\d{1,3}/\d+"
# 这里通过?:定义成非捕获分组


# 新的写法在这里
# pattern = fr"[A-Z]\S+\d+\s+({ipv4_basic})\s+(down|up)\s+(down|up)"

pattern = re.compile(
    rf'^(?P<interface>\S+)\s+'
    rf'(?P<ip_address>unassigned|{ipv4_basic})\s+'
    r'(?P<physical>\*?down|up)\s+'
    r'(?P<protocol>\*?down|up)\s*$'
)
match = pattern.match(display_ip_interface_brief_line)

if match:
    interface = match.group('interface')
    ip_address = match.group('ip_address')
    physical = match.group('physical')
    protocol = match.group('protocol')
    title_list = ['Interface','IP Address/Mask','Physical','Protocol']
    str_format = "|  {:<20}|  {:<20}|  {:<20}|  {:<20}|"
    # 这个就是格式，左边预留2格
    print(str_format.format(*title_list))
    print(str_format.format(interface, ip_address, physical, protocol))
else:
    print("No Match Found.")




