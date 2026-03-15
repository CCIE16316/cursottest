import re

# 1.1 | 或关系
result1 = re.match(r'Root|root', 'Root')
# result1 = re.match(r'[Rr]oot', 'Root')
print(result1)
# 或的关系

# 1.2 $以这个结尾
result2 = re.match(r'.*aries$', 'jinkinaries')
print(result2)
# 以aries结尾


