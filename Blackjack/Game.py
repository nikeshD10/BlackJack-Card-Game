

from BlackJackConfig import *

while True:
    # print an opening statement
    print("Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
           Dealer hits until she reaches 17. Aces count as 1 or 11")
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips() # remember the default value is 100
    # Prompt the Player for their bet
    take_bet(player_chips)
    # show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing: # recall this variable from our hit_or_stand function
        # Prompt for player to Hit or Stand
        hit_or_stand(deck, player_hand)
        # Show cards(but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    #Inform Player of their chips total
    print("\nPlayer's winnings stand at", player_chips.total)
    # Ask to play again
    new_game = input("Would you like to play an other hand? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break