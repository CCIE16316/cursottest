import random
from art import logo

def deal_card():
    """Returns a random card freom the desk"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def caculate_score(cards=list):
    """Take a list of cards and return the scorpe calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0    
    if 11 in cards and sum(cards) > 21: # 如果11在，并且已经超过21了，那么11就作为1去计算。
        cards.remove(11) 
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, oppent has Blackjack."
    elif u_score == 0:
        return "Win with a Blackjack."
    elif u_score > 21:
        return "Your went over. You lose."
    elif c_score > 21:
        return "Opponent went over. You win."
    elif u_score > c_score:
        return "You win."
    else:
        return "You Win."



def play_game():
    print(logo)

    user_cards = []
    computer_cards = []

    is_game_over = False

    for _ in range(2): # _ 代表不需要这个变量而已
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        # print(user_cards)
        # print(computer_cards)

        user_score = caculate_score(user_cards)
        computer_score = caculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score {user_score}.")
        print(f"Computer first cards: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = caculate_score(computer_cards)


    result = compare(user_score,computer_score)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    result = compare(user_score,computer_score)
    print(result)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()

