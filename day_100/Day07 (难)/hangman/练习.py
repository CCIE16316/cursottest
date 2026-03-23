import dis
from operator import le
import random
from re import L
from hangman_words import word_list
from hanman_art import stages,logo

print(logo)
print("Word to guess: _____")



chosen_words = random.choice(word_list)
print(chosen_words)
word_length = len(chosen_words)
# print(word_length)



placeholder = ""
for letter in range (word_length):
    placeholder += "_" # 这边是str所以不能像List一样用append。
print(placeholder)

lives = 6
correct_words = []
game_over = False
while not game_over:
    display = ""
    guess = input("Guess a letter: ")

    if guess not in chosen_words:
        lives -= 1
        print(f"You only have {lives}/6 Lives")
        print(stages[lives])
        if lives == 0:
            game_over = True
            print("GAME OVER!")


    for letter in chosen_words:
        if letter == guess:
            display += letter
            correct_words.append(letter)
        elif letter in correct_words:
            display += letter
        else:
            display += "_"
    if display == chosen_words:
        print("You Win!")
    if "_" not in display:
        game_over = True


    print(display)