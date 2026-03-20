# word_list = ["aardvark","baboon","camel"]
word_list = ["aaabbbccc"]

import dis
from mimetypes import guess_type
from operator import le
import random

# Task1 随机选择1个列表中的单词
chosen_word = random.choice(word_list)
print(chosen_word)

# Task2 根据选择单词打印placeholder
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Task3 
correct_letters = []
game_over = False
while not game_over:
    guess = input("Guess a letter:  ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if "-" not in display:
        game_over = True
        print("You Win!")
    print(display)





