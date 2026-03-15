import re


# 1.5 匹配任何看不见的，包括空格、制表符、换页符等空白字符的其中任意一个。
result5 = re.match(r'\s', ' ')
print(result5)
# 匹配任何看不见的

# 1.6 匹配任何看的见的。
result6 = re.match(r'\S', 'W')
print(result6)
# 匹配任何看不见的

# 1.7 最强匹配，[\s\S]代表要么看得见，要么看不见。
result7 = re.match(r'[\s\S]+', r'asdasda sd12312312312321\12\3123123k123\nms\s')
print(result7)
# 匹配任何看不见的
# .* 不行，因为多行内容无法显示
# . 是除换行以内的任意