# 1.0 大小写
str10 = "what makes it special in your eyes.TEST"
print(str10)
print(str10.capitalize())
# 首字母大写
print(str10.lower())
# 小写
print(str10.upper())
# 大写

# dir(str) 可以查看帮助

# 1.1 替换操作
str1 = "what makes it special in your eyes.TEST"
str2 = str1.replace('makes','jinkin')
print(str2)
# 替换makes到jinkin
str3 = str1.replace('makes','')
print(str3)
# 把makes剪切掉

# 1.2 找到下边缘位置
str4 = str1.find('makes')
print(str4)
# 这要就可以找到makes的启示位置，这里从0开始到5，正好在m这个字符

# 1.3 剥离
str5 = '\n\twelcome to qytang\n\r\t'
print(str5)
str6 = str5.strip()
print(str6)
# 剥离两边的空白
# \n newline 换行
# \r carriage return 回车
# \t tab 制表符，其实就是tab

# 1.4 更改字符串大小写+字符串连接
str7 = list(str5)
print(str7)
# 更改成列表区修改大小写
str7[3] = "E"
print(str7)
# 就变成大写E了
str8 = ''.join(str7)
print(str8)
# 再把字符串连接到一起