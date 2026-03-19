height = int(input("What is your height: "))
age = int(input("How old are you? "))
if height > 120:
    print(f"You can ride.")
    if age > 18:
        print(f"Plase give me $12.")
    else:
        print(f"please give me $7")
else:
    print(f"Your cant't ride.")

