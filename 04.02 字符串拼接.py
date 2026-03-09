# Str是不可变对象
str_xx = "Jinkin"
str_xx[0] = "j"
# 这样是不可行的，无法更改的

#1.1 字符串拼接
str1 = "jinkin"
str2 = "Baby"
str3 = str1 + " " + str2
print(str3)
# 字符串拼接

str4 = '=' * 20
print(str4)
# 一般用来格式打印

length_1 = len(str4)
length_2 = len(['aa','bb','cc','dd'])
print(length_1)
# 看Str的长度，这里是20个字符
print(length_2)
# 查看列表长度，这里是4个位置，分别对应0-3.


#1.2 字符串截取
myjob = 'hacker'
for i in myjob:
    print(i)
# for循环逐字打印
# 就是从myjob这个变量的值里面每次提取一个字符放到i里面，然后打印i加换行。

myjob = 'hacker'
for i in myjob:print(i, end='')
# 默认不换行，其他和上面一样

print('\n','='*12)
str_jk = 'welcome to shanghai'
print(str_jk[0])
# 这里0号位就是w，序列都有位置的，从0开始。

print('\n','='*12)
str_jk = 'welcome to shanghai'
print(str_jk[0:7])
# 从0到6，也就是welcome，其实是包含0，不包含7。
# [0, 7)：左闭右开区间
print(str_jk[-1])
# 从后往前第一个
print(str_jk[:])
# 全要
print(str_jk[3:])
# 从3到最后

