import random



suits = ['♣', '♦', '♥', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(rank, suit) for rank in ranks for suit in suits]

   


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
                return True
        elif action == "stand":
            return True
        else:
            print("Invalid action. Please choose either hit or stand")

    
def house_turn(house_hand):
    while hand_value(house_hand) < 17:
        print(f"Dealers hand: {house_hand}, total value: {hand_value(house_hand)}")
        house_hand.append(deal_card())

    print(f"Dealers hand: {house_hand}, total value: {hand_value(house_hand)}")
    print("------------------------------")

    if(hand_value(house_hand) > 21):
        #print("Dealer bust!")
        return False
    return True


    


def determine_winner(player_hand, house_hand):
    player_value = hand_value(player_hand)
    house_value = hand_value(house_hand)
    if(player_value > 21):
        print("Bust. You lose!")
    elif(house_value > 21):
        print("Dealer bust. You win!")
    elif(player_value > house_value):
        print("You win!")
    elif(house_value > player_value):
        print("You lose!")
    elif(player_value == house_value):
        print("tied game.")




def begin_game():

    print("===========================================")
    print("Welcome to Blackjack")
    print("===========================================")

    random.shuffle(deck)
    
    player_hand, house_hand = initial_deal()


    player_turn(player_hand)
    if(hand_value(player_hand) == 21):
       return

    house_turn(house_hand)
       
    
    determine_winner(player_hand, house_hand)
    


    

    



begin_game()
    





