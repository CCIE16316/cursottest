import random

# 1. 词表和艺术字
#import hangman_words
from hangman_words import word_list #这样就把word_list当本地使用了
from hanman_art import stages, logo


print(logo)
                               

# 2. 随机选择1个单词
lives = 6
chosen_word = random.choice(word_list)
# chosen_word = random.choice(hangman_words.word_list) 如果我们用import hanman_words，那么必须使用这种方式导入

print(chosen_word)

# 3. 添加占位符
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "-"
print(placeholder)


# 5. 显示内容，循环显示
corrent_letter = []
game_over = False
while not game_over:
    print(f"**********{lives}/6 LIVES LEFT**************************")
    guess = input("Guess a letter: ").lower()

    if guess in corrent_letter:
        print(f"You've already guessed {guess}")

    display = "" # aa____a__
    for letter in chosen_word: # a-a-r-d-v-a-r-k
        if letter == guess:
            display += guess
            corrent_letter += guess
        elif letter in corrent_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"Your guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"**********IT WAS {chosen_word}! YOU LOSE**********")

    if "_" not in display:
        game_over = True
        print("**********YOU WIN**********")

    print(stages[lives])