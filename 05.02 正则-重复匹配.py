import re
# 1.8 [] 匹配
result8 = re.match('a[a-z]c', 'abc')
# result8 = re.match('a[a-z]c', 'abc') 小写
# result8 = re.match('a[A-Z]c', 'abc') 大写
# result8 = re.match('a[a-zA-Z]c', 'abc') 小写到大写
# result8 = re.match('a[a-zA-Z0-9]c', 'abc') 小写到大写
# result8 = re.match('a[^0-9]c', 'abc') 不是整数
print(result8)
# 匹配任何看不见的

# 1.9 重复n次
result9 = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '192.168.22.3')
# result9 = re.match(r'\d{1,}\.\d{1,}\.\d{1,}\.\d{1,}', '192.168.22.3') 至少1次
# result9 = re.match(r'\d{2}\.\d{2}\.\d{2}\.\d{2}', '192.168.22.3') 2次
print(result9)
# 重复1-3次


# 1.10 + 至少出现1次
result10 = re.match(r'\d+\.\d+\.\d+\.\d+', '111.111.111.111')
print(result10)
# 至少重复1次


# 1.11 * 包含0次和无数次
result11 = re.match(r'\d*\.\d*\.\d*\.\d*', '2.2.2.2')
print(result11)
# 包含0次和无数次

# 1.12 * 包含0次和1
result12 = re.match(r'\d?\.\d?\.\d?\.\d?', '1.1.1.1')
print(result12)
# 至少重复1次

# 1.13 ()范围重复
result13 = re.match(r'ba(na)+', 'banana')
print(result13)
# na重复至少1次





