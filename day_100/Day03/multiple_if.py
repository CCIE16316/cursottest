height = 121
age = 15

if height >= 120:
    print("you can ride.")
    if age <= 12:
        bill = 5
        print("Child -> $5")
    elif age <= 18:
        bill = 7
        print("Youth -> $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller brfore you can ride.")



