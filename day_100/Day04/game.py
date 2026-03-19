import random

result = ["Rock","Paper","Scissors"]
choice_people = int(input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors."))
choice_computer = random.randint(0,2)

if choice_people == choice_computer:
    print(f"{result[choice_people]} vs {result[choice_computer]}, It's a draw.")
elif choice_people >=3 or choice_people <0:
    print("Wrong Number")
else:
    if choice_people == 1 and choice_computer == 0:
        print(f"People Choice:{result[choice_people]} vs. Computer Choice:{result[choice_computer]}, You Win!")
    elif choice_people == 2 and choice_computer == 1:
        print(f"People Choice:{result[choice_people]} vs. Computer Choice:{result[choice_computer]}, You Win!")
    elif choice_people == 0 and choice_computer == 2:
        print(f"People Choice:{result[choice_people]} vs. Computer Choice:{result[choice_computer]}, You Win!")
    else:
        print(f"People Choice:{result[choice_people]} vs. Computer Choice:{result[choice_computer]}, You Lost!")