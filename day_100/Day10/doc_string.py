def format_name(f_name=str, l_name=str):
    """
    Take a first and last name and format it to return the titile case version of the name.
    """
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"Result: {format_f_name} {format_l_name}" # 函数返回的结果
    print("111") # Return是结束语，后面内容不会显示

formated_string = format_name(input(f"{'What is your firstname: ':>25}"),input(f"{'What is your lastname: ':>25}")) # 承载函数的结果
print(formated_string) # 打印函数的结果


# 上面增加了docsstring，其实就是我们按ctrl 然后点formated_string就可以显示注释了。
