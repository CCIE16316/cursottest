def format_name(f_name=str, l_name=str):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"Result: {format_f_name} {format_l_name}" # 函数返回的结果
    print("111") # Return是结束语，后面内容不会显示

formated_string = format_name(input(f"{'What is your firstname: ':>25}"),input(f"{'What is your lastname: ':>25}")) # 承载函数的结果
print(formated_string) # 打印函数的结果



# 如果这样的话那么我们一个函数就解决一个问题
# 1. 比如我们可以做一个函数就是把别人大小写乱序的名字改成，大写开头。
# 2. 比如我们第二个就是合并文字的。 etc.

