height = int(input("Height? "))
if height <= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("$5")
    elif age <= 18:
        print("$7")
    else:
        print("$12")    
        # 这里一点点把范围收紧。
else:
    print("srry you have to grow taller before you can ride.")