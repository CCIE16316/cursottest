from operator import le
import string
import random

print(f"Welcome to the PyPassword Generator!")

all_letter = list(string.ascii_letters)
all_symbol = list(string.punctuation)
all_number = list(string.digits)

rand_letter = random.randint(0,len(all_letter)-1)
rand_symbol = random.randint(0,len(all_symbol)-1)
rand_number = random.randint(0,len(all_number)-1)




letter = int(input("How manay letters would you like in your password? "))
symbol = int(input("How many symbols would you like? "))
number = int(input("How many numbers would you like? "))




# Print(f"Your password is: {}")