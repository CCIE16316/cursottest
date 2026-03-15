import re

# 1.4 匹配 \w 大写、小写、数字、下划线
result4 = re.match(r'\d\w\w', '1_a')
print(result4)