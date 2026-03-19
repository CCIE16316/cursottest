print(10 % 5)
print(10 % 4) 
# 取模4，那么2x4=8，那么余2 
# 10 / 4 = 2R2

number_to_check = int(input("What is the number you want to check?"))
if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")
# 取模偶数，那么输入的数必须是偶数
# 这里就可以判断是否是偶数还是奇数
