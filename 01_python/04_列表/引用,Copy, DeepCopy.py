import copy
# 1 引用，原始列表修改，那么引用的列表内的内容也跟着修改
x = [1,2,3] # 内存空间放了一个列表
l1 = [10,11,x,12] # 引用了x其实是引用，在内存空间里面就是指针指向到x的内存空间。
print(l1)
x[1] = 'aa' # 修改1号位置
print(l1) # 这里打印后发现已经被修改了


# 2 Copy 
l2 = [2,3,4,5,6]
l3 = l1



# 3 DeepCopy 把嵌套内的引用也复制
l4 = [1,2,3,4,5]
print(l4)
l5 = copy.deepcopy(l4)
print(l5)
l5.append('a')
print(l5)