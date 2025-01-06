import random
import sys
import os
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # 'cls' for Windows, 'clear' for Mac/Linux


suits = ['♣', '♦', '♥', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(rank, suit) for rank in ranks for suit in suits]

   


def handle_endgame():
    while True:  # Create a loop that runs until a valid input is received
        q = input("Would you like to play again?(y/n): ").strip().lower()  # Ensure input is case-insensitive and trimmed
        if q == "y":
            print("Starting a new game!...")  # Inform the user
            time.sleep(0.4)  # Delay for 0.7 seconds (adjust as needed)
            clear_terminal()  # Clear the terminal
            begin_game()  # Start a new game
            break
        elif q == "n":
            print("Thanks for playing! Goodbye! 👋")
            sys.exit()
        else:
            print("Sorry, I didn't get that. Please enter 'y' or 'n'.")




def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])

def deal_card():
    return deck.pop()


def initial_deal():
    player_hand = [deal_card(), deal_card()]
    house = [deal_card(), deal_card()]
    return player_hand, house


def hand_value(hand):

    value = 0

    for card in hand:
        value += card_value(card)
    return value
    


def player_turn(player_hand):
    while True:
        print(f"Your hand: {player_hand}, total value: {hand_value(player_hand)}")

        if(hand_value(player_hand) == 21):
            print(f"Your hand: {player_hand}, total value: {hand_value(player_hand)}")
            print('🎊 BAM! 🎆 You hit 21, the blackjack jackpot! 🃏💥')
            handle_endgame()
        
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        print("------------------------------")

        if action == "hit":
            player_hand.append(deal_card())
            if hand_value(player_hand) > 21:
                print(f"Your hand: {player_hand}, total value: {hand_value(player_hand)}")
                #print(f"you bust! Game over")
                return False
            elif (hand_value(player_hand) == 21):
                print('🎊 BAM! 🎆 You hit 21, the blackjack jackpot! 🃏💥')
                handle_endgame()
        elif action == "stand":
            return True
        else:
            print("Invalid action. Please choose either hit or stand")

    
def house_turn(house_hand):
    while hand_value(house_hand) < 17:
        house_hand.append(deal_card())

    
    print(f"Dealers final hand: {house_hand}, total value: {hand_value(house_hand)}")
    print("------------------------------")

    if(hand_value(house_hand) == 21):
        print("🎲 UH OH. Dealer hits 21 🎊. You Lose!🃏💥")
        handle_endgame()

    if(hand_value(house_hand) > 21):
        #print("Dealer bust!")
        return False
    return True


    


def determine_winner(player_hand, house_hand):
    player_value = hand_value(player_hand)
    house_value = hand_value(house_hand)
    if(player_value > 21):
         print(f'🎮 You’ve gone bust with a total of {hand_value(player_hand)}. Better luck next time! 💔🎭')
    elif(house_value > 21):
        print(f"🎲 Oh no...I’ve gone bust with a total of 💸{hand_value(house_hand)}. The win is yours! 🎉.")
    elif(player_value > house_value):
        print("🎮 You win! 👏👑")
        handle_endgame()
    elif(house_value > player_value):
        print("🎲 You lose! Better luck next time. 💼😉")
        handle_endgame()
    elif(player_value == house_value):
        print("🤷‍♂️🤷 tied game. 🤝")
        handle_endgame()




def begin_game():

    
    print("=" * 50)
    print("                  Welcome to Blackjack                  ")
    print("=" * 50)

    

    action = input("Press g to play: ")

    if action == "g":
        random.shuffle(deck)
        player_hand, house_hand = initial_deal()

        #Deal with player bust

        print(f"Dealers initial hand: {house_hand}, total value: {hand_value(house_hand)}")
        if(hand_value(house_hand) == 21):
           print("🎲 UH OH. Dealer hits 21 🎊. You Lose!🃏💥")
           handle_endgame()


        if not(player_turn(player_hand)):
            print(f'🎮 You’ve gone bust with a total of 🃏{hand_value(player_hand)}🃏. Better luck next time! 💔🎭')
            print("------------------------------")
            handle_endgame()
            
    
    
        if not(house_turn(house_hand)):
            print(f"🎲 Oh no...I’ve gone bust with a total of 🃏{hand_value(house_hand)}🃏. The win is yours! 🎉.")
            print("------------------------------")
            handle_endgame()
        
        determine_winner(player_hand, house_hand)

    else: 
        print("Invalid action.")


    



    


    

    
       
    
    


    

    



begin_game()
    





