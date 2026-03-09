# 新版格式化方法

import stat


ip_address = '1.1.1.1'
interface = 'gi1'
status = 'up'
protocol = 'down'
money = '3.123'
result = f"{interface:<30} {ip_address:<30} {status:<30} {protocol:<30} {money:2f}"
print(result)
# 这个就比老的方法轻松多了，老的方法一旦规模大就很混乱。


