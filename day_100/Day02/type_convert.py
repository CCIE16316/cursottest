print(int("1234")+int("12345"))
# str转换成了int了


# Example 1
# print("Number of the letters in your name: " + len(input("Enter your name: ")))
# 这个有错误，前面是str，后面len其实是int，两个无法相加。

length = (len(input("Enter your name: ")))
print("Number of the letters in your name: " + str(length))
# 这里转换成str就行了

