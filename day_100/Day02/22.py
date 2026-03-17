print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $ "))
tips = int(input("how much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
# print(type(bill))
# print(type(tips))
each = bill * ( 1 + tips / 100) # 给消费，比如15元tips，那么就是％0.15
round_each = round(each,2) # 四舍五入到小数点第二位

print(f"Each person should pay: ${round_each}")