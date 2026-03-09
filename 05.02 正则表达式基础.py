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

# 1.3 匹配IP地址
result3 = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '192.168.22.3')
print(result3)
# 这样就是\d，匹配一个数字0-9，出现1-3次。

# 1.4 匹配 \w 大写、小写、数字、下划线
result4 = re.match(r'\d\w\w', '1_a')
print(result4)

# 1.5 匹配任何看不见的，包括空格、制表符、换页符等空白字符的其中任意一个。
result5 = re.match(r'\s', ' ')
print(result5)
# 匹配任何看不见的

# 1.6 匹配任何看的见的。
result6 = re.match(r'\S', 'W')
print(result6)
# 匹配任何看不见的

# 1.7 最强匹配，[\s\S]代表要么看得见，要么看不见。
result7 = re.match(r'[\s\S]+', 'asdasda sd12312312312321\12\3123123k123\nms\s')
print(result7)
# 匹配任何看不见的
# .* 不行，因为多行内容无法显示
# . 是除换行以内的任意
