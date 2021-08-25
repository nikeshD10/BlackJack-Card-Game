#Import random for the suffle
import random
# Declare the Variables to store suits, ranks and values
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
         "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9,
          "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}
#Decalaring the boolean True to control while loops and control the flow of the game
playing = True

# Creating the Card class where each card object has a suit and a rank.Later on after creating
# hand class we will handle value their.
# Consists two methods __init__ and __str__ so that when asked to print Card, returns a string
# in the form "Two of Hearts"
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"
# Creating the class Deck
# Store 52 card objects in a list that can later be shuffled.
# First we need to instantiate(represent as) all 52 unique card objects and add them to our list
# Build Card objects inside our Deck __init__ method.
# Iterate over sequences of suits and ranks to build out each card.
# Might appear inside a Deck class __init__ method:
# We want to add methods to shuffle our deck adn to deal out cars during gameplay.
class Deck:
    def __init__(self):
        # Note init is not taking a deck as a parameter because when we initialize deck of card we wanna it to be same
        # every time. We don;t wanna use it to input the parameter or make something different with deck.
        # Instead deck should one of the standarized thing.
        self.deck = [] # Start with the empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))#Build Card objects and add them to the list

    def __str__(self):
        # we can composing deck as a string so we call card_list_as_str variable which is deck composition
        card_list_as_str = " " # Start with an empty string
        for card in self.deck:
            #print(card)
            card_list_as_str += "\n" + card.__str__()
        return "The deck has: " + card_list_as_str

    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        # It is going to grab a card from self.deck attribute which is list of card object
        single_card = self.deck.pop()
        return single_card
#test_deck = Deck()
#print(test_deck)


# Creating a Hand class
# The Hand class may be used to calculate the value of those cards using the values dictionary defined above.
# It may also need to adjust for the values of Aces when appropriate.

class Hand: #going to calculate the value of hand.
            #What we will able to do is pass in actual rank of card and get back value of card
            #represent what cards is in someone hands

    def __init__(self):
        self.cards = []  # Start with an empty list as we did in the Deck class and add card from deck
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track od aces
    def add_card(self, card):
        # we are going to call deal from Deck class and grab that single card and add to someone hands which we do in
        # add_card method
        # Note card passed in below is from Deck.deal(). It is single Card object which have suit and rank. We get the
        # rank attribute from card object.
        # Here the card looks like card = self.deck.pop()
        self.cards.append(card)
        #self.value = values[card.rank]# this step helps to get the numeric value from string number stored inside values
                                      # dictionary
        #print(self.value)# This print numeric value of number. Output:- 4
        self.value += values[card.rank]
        #print(card.rank)# This print string value of number. Output:- four
        if card.rank == "Ace":
            self.aces += 1 # add to self.aces
    #Great! let's tackle the Aces issue. If a hand's value exceeds 21 but it contains an Ace, we can reduce the Ace's
    #value from 11 to 1 and continue playing.
    """
        Adjsuting for  a ace.
        self.aces allows us to keep the track of the number of aces we have
        So inside of the add_card method we can track the aces
    """
    def adjust_for_ace(self):
        # while my value is > 21 and still have aces then substract 10 from it and then take my aces
        # and take out my one from ace
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Creating a Chips class
# To keep track of a player's starting chips, bets, and ongoing winnings
#
class Chips:
    def __init__(self):
        self.total = 100 # This can be set to a default value or supplied by a user input
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet
"""test_deck = Deck() 
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
#print(test_player.value)
for card in test_player.cards:
    print(card)"""
# Writing a function for taking bets
#  Since we're asking the user for an integer value, this would be a good place to use try/except
# Remember to check that a Player's bet can be covered by their available chips
# Now the many of steps are going to be repetitive where we use global function

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break

"""
    Function for taking hits.
    Either player can take hits until they bust. This function will be called during gameplay
    anytime a Player requests a hit, or a Dealer's hand is less than 17. It should take in Deck
    and Hand objects as arguments, and deal one card off the deck and add it to the Hand.
    We may want it to check for aces in the event that a player's hand exceeds 21
"""

def hit(deck, hand):
    hand.add_card(deck.deal()) # We can also do single_card = deck.deak()
                               # hand.add_card(deck.deak())
    hand.adjust_for_ace() # Check for ace suggestment

# Writing a function prompting the Player to Hit or Stand
"""
    This function should accept the deck and the player's hand as arguments, and assign playing
    as a global variable. If the player Hits, employ the hit() function above. If the player
    Stands, we set the playing variable to False - this will control the behavior of a while 
    loop later on in our code.
"""
"""
    write a function prompting the player to hit or stand
    Accept deck and player hand as an argument  and assign 'playing' as a global variable
    
"""
def hit_or_stand(deck, hand):
    global playing # to control an upcoming while loop
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        if x[0].lower() == 'h':
            hit(deck, hand) # hit() function defined above
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing")
            playing = False
        else:
            print("Sorry, please try again")
            continue
        break

"""
    Write functions to display cards
    When a game starts, and after each time Player takes a card, the dealer's first card is hidden
    and all of Player's cards are visible. At the end of the hand all cards are shown, and you 
    may want to show each hand's total value. Write a function for each of these scenarios.
"""

def show_some(player, dealer):
    print("\nDealer's Hand: ")
    print(" One card hidden! ")
    print(" ", dealer.cards[1])
    #We can do print("\nPlayer's Hand: ", *player.cards, sep="\n")
    print("Players hand: ")
    for card in player.cards:
        print(card)
def show_all(player, dealer):
    """We can do this also
    print("\nDealer's Hand: ", *dealer.cards, sep="\n")
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep="\n")
    print("Player's Hand = ", player.value)"""
    print("Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("Player's hand: ")
    for card in player.cards:
        print(card)
"""
    QUICK NOTES ABOUT PRINT STATEMENTS:
    * The asterisk * symbol is used to print every item in a collection, and the sep="\n" 
      argument prints each item on a separate line.
    * In the fourth line where we have:
            print("",dealer.cards[1])
      the empty string and comma are there just to add a space.
    * Here we used commas to separate the objects being printed in each line. If you want to
      concatenate strings using the + symbol, then you have to call each Card object's 
      __str__ method explicitly, as with
            
            print(" " + dealer.cards[1].__str__())
"""

# Writing a functions to handle end of game scenarios
# Remember to pass player's hand, dealer's hand and chips as needed
# to handle each of game situation where it is going to end

def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player tie! It's a push.")

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

    # If player's hand exceeds 21, run player_busts() and break out of loop
    if player_hand.value > 21:
        player_busts(player_hand, dealer_hand, player_chips)
        break
    if player_hand.value <= 21:

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
    print("\nPlayer total chips are at: {} ".format(player_chips.total))
    # Ask to play again
    new_game = input("Would you like to play an other hand? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break



