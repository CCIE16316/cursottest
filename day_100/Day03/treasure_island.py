print('''     _ _       _    _       _       
    | (_)_ __ | | _(_)_ __ | | __   
 _  | | | '_ \| |/ / | '_ \| |/ /   
| |_| | | | | |   <| | | | |   <    
 \___/|_|_| |_|_|\_\_|_| |_|_|\_\   
                                     ''')

print(f"Welcome to Treasure Island.\nYour missions is to find the treasure.")
left_right = input("left or right? ")
if left_right == "right":
    print("Game Over! ")
else:
    swim_wait = input("Swim or Wait? ")
    if swim_wait == "swim":
        print("Game Over! ")
    else:
        which_door = input("Which Door? ")
        if which_door == "blue" or which_door == "red":
            print("Game Over! ")
        else:
            print("You Win")




