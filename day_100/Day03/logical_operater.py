height = int(input("Height? "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("$5")
    elif age <= 18:
        print("$7")
    elif age >= 45 and age <=55: # 这里用逻辑与
        print("Free $0")
else:
    print("sorry you have to grow taller before you can ride.")