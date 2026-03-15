# 1.1 转义符 \
import re
result = re.match('cmd.exe', 'cmdaexe')
# 匹配cmd.exe，这里的.是匹配任意字符（除换行外），所以我们cmdaexe就匹配上了。
print(result)
result1 = re.match(r'cmd\.exe', 'cmdaexe')
print(result1)
# r表示原始字符串，如果不加r，要写成\\.才能转义，
# python \代表转义，但是传递到正则引擎后再次被认为是\转义，可能就理解成其他东西了，所以用r关闭python哪一层的转义。

# 1.2 \d 代表匹配一位数字
result2 = re.match(r'cmd\dexe', 'cmd1exe')
print(result2)
# \d代表一位数字0-9




