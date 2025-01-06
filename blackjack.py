import random
import sys
import os
import time

cash = 0
total_wins = 0
total_losses = 0

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # 'cls' for Windows, 'clear' for Mac/Linux


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

def deal_card(deck):
    return deck.pop()


def initial_deal(deck):
    player_hand = [deal_card(deck), deal_card(deck)]
    house = [deal_card(deck), deal_card(deck)]
    return player_hand, house


def hand_value(hand):
    # Calculate the initial value of the hand
    value = 0
    aces = 0  # Count the number of Aces in the hand

    for card in hand:
        if card[0] == 'Ace':
            aces += 1
            value += 11  # Assume Ace is 11 initially
        else:
            value += card_value(card)  # Add the value of non-Ace cards

    # Adjust Aces if the total value exceeds 21
    while value > 21 and aces > 0:
        value -= 10  # Convert one Ace from 11 to 1
        aces -= 1

    return value

    


def player_turn(player_hand, deck):
    global total_wins, total_losses
    while True:
        print(f"Your hand: {player_hand}, total value: {hand_value(player_hand)}")

        if(hand_value(player_hand) == 21):
            print('🎊 BAM! 🎆 You hit 21, the blackjack jackpot! 🃏💥')
            total_wins += 1
            print(f"🏆 Total Wins: {total_wins} | ❌ Total Losses: {total_losses}")
            return True
        
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        print("------------------------------")

        if action == "hit":
            player_hand.append(deal_card(deck))
            if hand_value(player_hand) > 21:
                print(f"Your hand: {player_hand}, total value: {hand_value(player_hand)}")
                #print(f"you bust! Game over")
                return False
            elif (hand_value(player_hand) == 21):
                print(f"Your hand: {player_hand}, total value: {hand_value(player_hand)}")
                print('🎊 BAM! 🎆 You hit 21, the blackjack jackpot! 🃏💥')
                handle_endgame()
        elif action == "stand":
            return True
        else:
            print("Invalid action. Please choose either hit or stand")

    
def house_turn(house_hand, deck):
    global total_wins, total_losses
    while hand_value(house_hand) < 17:
        house_hand.append(deal_card(deck))

    
    print(f"Dealers final hand: {house_hand}, total value: {hand_value(house_hand)}")
    print("------------------------------")

    if(hand_value(house_hand) == 21):
        print("🎲 UH OH. Dealer hits 21 🎊. You Lose!🃏💥")
        total_losses += 1
        print(f"🏆 Total Wins: {total_wins} | ❌ Total Losses: {total_losses}")
        handle_endgame()

    if(hand_value(house_hand) > 21):
        #print("Dealer bust!")
        return False
    return True


    


def determine_winner(player_hand, house_hand):
    
    global total_wins, total_losses  # Use the global variables

    player_value = hand_value(player_hand)
    house_value = hand_value(house_hand)

    if player_value > 21:
        print(f'🎮 You’ve gone bust with a total of {player_value}. Better luck next time! 💔🎭')
        total_losses += 1  # Increment losses
    elif house_value > 21:
        print(f"🎲 Oh no...I’ve gone bust with a total of {house_value}. The win is yours! 🎉.")
        total_wins += 1  # Increment wins
    elif player_value == 21 and house_value == 21:
        print("🤝 It's a tie! Both you and the dealer hit 21. Well played! 🌟")
    elif player_value == house_value:
        print("🤷‍♂️🤷 It's a tied game. 🤝")
    elif player_value > house_value:
        print("🎮 You win! 👏👑")
        total_wins += 1  # Increment wins
    else:
        print("🎲 You lose! Better luck next time. 💼😉")
        total_losses += 1  # Increment losses

    print(f"🏆 Total Wins: {total_wins} | ❌ Total Losses: {total_losses}")  # Display stats
    handle_endgame()






def begin_game():

    global total_wins, total_losses

    suits = ['♣', '♦', '♥', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    
    print("=" * 50)
    print("                  Welcome to Blackjack                  ")
    print("=" * 50)


    while True:  # Loop until the user provides a valid input
        action = input("Press 'g' to play: ").strip().lower()
        if action == "g":
            break  # Exit the loop if the input is valid
        else:
            print("Invalid action. Please press 'g' to start the game.")

    if action == "g":


        random.shuffle(deck)
        player_hand, house_hand = initial_deal(deck)

        #Deal with player bust

        print(f"Dealers initial hand: {house_hand}, total value: {hand_value(house_hand)}")
        if(hand_value(house_hand) == 21):
           print("🎲 UH OH. Dealer hits 21 🎊. You Lose!🃏💥")
           total_losses += 1
           print(f"🏆 Total Wins: {total_wins} | ❌ Total Losses: {total_losses}")
           handle_endgame()


        if not(player_turn(player_hand, deck)):
            print(f'🎮 You’ve gone bust with a total of 🃏{hand_value(player_hand)}🃏. Better luck next time! 💔🎭')
            total_losses += 1
            print(f"🏆 Total Wins: {total_wins} | ❌ Total Losses: {total_losses}")
            print("------------------------------")
            handle_endgame()
            
    
    
        if not(house_turn(house_hand, deck)):
            print(f"🎲 Oh no...I’ve gone bust with a total of 🃏{hand_value(house_hand)}🃏. The win is yours! 🎉.")
            total_wins += 1
            print(f"🏆 Total Wins: {total_wins} | ❌ Total Losses: {total_losses}")
            print("------------------------------")
            handle_endgame()
        
        determine_winner(player_hand, house_hand)

    else: 
        print("Invalid action.")


    


    



begin_game()
    





