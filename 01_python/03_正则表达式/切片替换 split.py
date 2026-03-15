import re

# 1.1 切片
result1 = re.split('-','aaa-bbb-ccc')
print(result1)
# 切分出了3个对象

# 1.2 不规则切片
result2 = re.split('[-=]+','aaa---bbb===ccc')
print(result2)
# 切分出了3个对象


