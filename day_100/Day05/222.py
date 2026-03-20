from operator import le
import string
import random

all_letter = list(string.ascii_letters)
all_symbol = list(string.punctuation)
all_number = list(string.digits)

print(f"Welcome to the PyPassword Generator!")

nr_letter = int(input("How manay letters would you like in your password? "))
nr_symbol = int(input("How many symbols would you like? "))
nr_number = int(input("How many numbers would you like? "))

# 1.1 简单版
list_new = []
for char in range(1,nr_letter + 1):
    # 如果nr_letter是4，那么就是range(1,5)，其实就是1、2、3、4轮
    list_new.append(random.choice(all_letter))

for char in range(1,nr_symbol + 1):
    # 如果nr_letter是4，那么就是range(1,5)，其实就是1、2、3、4轮
    list_new.append(random.choice(all_symbol))

for char in range(1,nr_number + 1):
    # 如果nr_letter是4，那么就是range(1,5)，其实就是1、2、3、4轮
    list_new.append(random.choice(all_number))


# print(''.join(list_new))
print(list_new)
shuffled_list = list_new.copy()
random.shuffle(shuffled_list)
print(''.join(shuffled_list))
