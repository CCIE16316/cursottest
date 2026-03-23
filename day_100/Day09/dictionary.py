programming_dictionary = {
    "Bug":"An Error in a program that prevents the program from running as expected.",
    "Function":"A Piece of code that you can eaily call over and over again.",
    }
# print(programming_dictionary["bug"]) # 这里大小写要看清楚，否则就会报错。
programming_dictionary["loop"] = "The action of doing something over and over again"
# print(programming_dictionary)
# programming_dictionary = {}
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)


for key in programming_dictionary:
    print(key) # 这里就是每次循环后输出的Key。
    print(programming_dictionary[key]) # 这里是每次循环输出的Key的Value。


# 注意事项：
# 1. 词典不能用append
# 2. 词典不能+=
# 