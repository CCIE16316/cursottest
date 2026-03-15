import re
# 1.3 匹配IP地址
result3 = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '192.168.22.3')
print(result3)
# 这样就是\d，匹配一个数字0-9，出现1-3次。