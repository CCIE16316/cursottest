# 1. 能被4整除吗？如果不能则是平年（365天）
# 2. 能被100整除吗？如果不能则是闰年（比如2024年）如果能（即世纪年，比如1900,2000年）则进入下一步。
# 3. 能被400整除吗？如果不能则是平年。如果能则是闰年，比如2000年。


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("What is current year?: "))
result = is_leap_year(year)
print(result)






