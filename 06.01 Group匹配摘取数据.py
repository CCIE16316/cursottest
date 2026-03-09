import re
# 1.1 案例
show_if = "GigabitEthernet1        192.168.2.1    YES NVRAM   up                  up"
result3 = re.match(r'[A-Z]\S+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\S+\s+\S+\s+\S+\s+\S+', show_if)
print(result3)
# 这里显示内容有极限，所以不能再显示了
# 如果我想要接口那么就按照下面操作
match = re.match(
    r'([A-Z]\S+)\s+'
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
    r'(\S+)\s+(\S+)\s+(\S+)\s+(\S+)',
    show_if,
)
if match:
    result4 = match.groups()
    print(result4)
    # 用()把需要的摘出来
    # 其实是一个元祖Array
    print(result4[0])
    print(result4[1])
    print(result4[2])



