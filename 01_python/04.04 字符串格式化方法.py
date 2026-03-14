# 一般我们show出来的内容都很有格式，很整齐，舒服
# 所以我们要把输出内容整理成四四方方的
# 0.1 已经过时的方法
from ipaddress import ip_address


str_format = '{},{} and {}'
result = str_format.format('a','b','c')
print(result)

result1 = '{0:10}={1:10}'.format('spam','123.4567')
print(result1)
# 第一个spam，也就是0号位，右边空10格
# 第二个123.4567，也就是1号位，右边空10格

result2 = '{:^10}={:<15}'.format('spam','123.4567')
print(result2)
# 0号位置，居中
# 1号位，右边移15个空格

result3 = '{:<10}{:<10}'.format('spam','123.4567')
print(result3)
# 0和1号都左对齐，一共10个格子的空间

# Example:
line_format = '{interface:30} {ip_address:25} {status:40} {protocol:10}'
result3 = line_format.format(interface="GigabitEthernet",ip_address="192.168.2.1",status="up",protocol="up")
print(result3)
# 所以这样都对齐了
# 上面可以写入成左右对齐的，比如{interface:<30}左对齐，{ip_address:>25}右对齐等
# 左右对齐主要看>方向，指向哪里就是向哪里对齐


# 1.1 浮点数技巧
f1 = 13.121312313
f2 = 1234.123123123
f3 = 4.21312312
result5 = '{:f}, {:.2f}, {:.3f}'.format(f1,f2,f3)
print(result5)
# 浮点数保留小数位,比如0号位置原汁原味，1号位保留2位，2号位保留3位。



