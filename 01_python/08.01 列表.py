# 1.1 任意内容放进列表
list1 = [1,2,3,'aaa',[1,'me',3],{1:1}]
print(list1)

# 1.2 字符串转换成列表
list2 = list('jinkin')
print(list2)
# 字符串转换成列表

# 1.3 列表包含array
list3 = list(range(5))
print(list3)
# 从0开始迭代到4


# 1.4 取值
list4 = list1[4][1]
print(list4)
# 取列表1里面4号位内的1号位内容

# 1.5 长度
len = len(list4)
print(len)
# 计算长度

# 1.6 Method
method1 = 'jinkin'.upper()
print(method1)
# 字符串内置的方法 ()不能漏

# 1.7 列表合并
list5 = list1 + list2
print(list5)

# 1.8 列表循环
for i in [1,2,3,4]:
    print(i,end='')
# 默认打印的时候是换行的
# 可以输入end=''不换行

# 1.9 列表解析式
res = [c * 4 for c in 'qyt']
print(res)
# 每次迭代出来的内容都乘以4


# 1.10 追加列表到队尾
test1 = []
for i in 'abc':
    test1.append(i*4)
    print(test1)
# 提取字符串，然后变成4倍，之后追加到[]队尾


