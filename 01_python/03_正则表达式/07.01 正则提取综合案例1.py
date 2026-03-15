import re

display_ip_interface_brief_line = "Vlanif20        20.1.1.254/24    up     up"
ipv4_basic = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d+"
# 这里的/就是斜杠
# ipv4_basic = r"(?:\d{1,3}\.){3}\d{1,3}/\d+"
# 这里通过?:定义成非捕获分组
pattern = fr"([A-Z]\S+\d+)\s+({ipv4_basic})\s+(down|up)\s+(down|up)"
#re_result = re.match(pattern,display_ip_interface_brief_line)
re_result = re.match(pattern,display_ip_interface_brief_line)
# print(re_result[1])
# print(re_result[2])
# print(re_result[3])
# print(re_result[4])
if re_result:
    result_list = re_result.groups()
    print(result_list)

title_list = ['Interface','IP Address/Mask','Physical','Protocol']
str_format = "|  {:<20}|  {:<20}|  {:<20}|  {:<20}|"
# 这个就是格式，左边预留2格
print(str_format.format(*title_list))
print(str_format.format(*result_list))
