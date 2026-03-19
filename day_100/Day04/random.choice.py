import random

friends = ["Jack","Leon","Alice","John"]

# Option 1
# rand_friend = random.randint(0,3)
# print(f"My Friend is {friends[rand_friend]}.")

# Option 2
print(f"My Friend is {random.choice(friends)}.")