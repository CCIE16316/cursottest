# from art import logo
# print(logo)
# print("Welcome to the secret auction program.")




# print("\n" * 100)

bids ={}
continue_price = False
while not continue_price:
    name = input("What is your name?:\n")
    price = int(input("What's your bid?:\n$"))
    bids[name] = price
    stop = input("Are there any other biders?Type 'yes' or 'no'.\n").lower()
    if stop == "no":
        continue_price = True
# print(bids)


max_value = max(bids.values())
# print(max_value)
for name,score in bids.items():
    if score == max_value:
        print(f"{name} is the highest score. {score}")



# print(f"The winner is James with a price of $142")