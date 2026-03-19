print('''     _ _       _    _       _       
    | (_)_ __ | | _(_)_ __ | | __   
 _  | | | '_ \| |/ / | '_ \| |/ /   
| |_| | | | | |   <| | | | |   <    
 \___/|_|_| |_|_|\_\_|_| |_|_|\_\   
                                     ''')

print(f"Welcome to Treasure Island.\nYour missions is to find the treasure.")


choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".').lower() # 都切换成小写，方便判断。

if choice1 == "left":
    choice2 = input('You\'ve come to a lake.' 
                    'There is an island in the middle of the lake.'
                    'Type "wait" to wait for a boat.'
                    'Type "swim" to swim across.').lower() # 都切换成小写，方便判断。
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed. "
                        "There is a hourse with 3 doors. One Red"
                        "one yellow and one blue."
                        "Which colour do you choose?").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == 'yellow':
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("Your enter a room of beasts. Game OVer.")
        else:
            print("Your chose a door that doesn't exist. Game Over.")
    else:
        print("Your got attacked by an angre trout. Game Over?")
else:
    print("Your fell into a hole. Game Over.")


# https://ascii.co.uk/art 
# 这个网站可以获取ASCII艺术，或者直接找AI生成。

