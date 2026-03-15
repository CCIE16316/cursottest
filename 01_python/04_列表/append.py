# 1 append
l1 = [1,2,3,4,5]
for i in 'abc':
    l1.append(i*4) # 第一次提取a，然后再l1这个列表尾部追加a*4，也就是aaa，然后第二轮bbb，第三轮ccc
    print(l1)

# 2 追加List
l2 = [1,2,3,4]
l3 = [5,6,7,8]
l2.append(l3) # append是追加到末尾，所以把整个list追加到L2里面去了 
print(l2)
# [1, 2, 3, 4, [5, 6, 7, 8]]
print(l2[-1])
# 打印列表最后尾部位置的内容