import re

port_list = [
    'eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7',
    'eth 1/101/2/46', 'eth 1/101/1/34', 'eth 1/101/1/18', 'eth 1/101/1/13',
    'eth 1/101/1/32', 'eth 1/101/1/25', 'eth 1/101/1/45', 'eth 1/101/2/8'
]

l1 = []
for i in port_list:
    y = tuple(map(int, re.match(r'^eth (\d+)/(\d+)/(\d+)/(\d+)$', i).groups()))
    l1.append(y)

# 先按整数元组排序
sorted_l1 = sorted(l1)

result = []
for y in sorted_l1:
    port = f"eth {y[0]}/{y[1]}/{y[2]}/{y[3]}"
    result.append(port)

print(result)