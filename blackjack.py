import random
from colorama import init, Fore, Back, Style
import os
import sys

# Colorama initialize 
init()

# This clears the terminal. cls for Windows and clear for unix. 
os.system('cls||clear')

suits = {
        'Hearts': '♥',
        'Clubs': '♣',
        'Spades': '♠',
        'Diamonds': '♦'
        } 

playing = True 

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()
        
    # Assign 
    def show(self):
        """Cards are valued between 1 and 14. 2 through 10 are literal values. The rest are as described below

        Returns:
            [str]: [Returns the suit and value combination]
        """        
        if self.value == 1:
            val = "A" #Ace
        elif self.value == 11:
            val = "J" #Jack
        elif self.value == 12:
            val = "Q" #Queen
        elif self.value == 13:
            val = "K" #King
        else:
            val = self.value

        red_col = Fore.RED
        black_col = Fore.BLACK
        white_bg = Back.WHITE
        reset = Style.RESET_ALL
        
        # handle red colors on Hearts and Diamonds 
        if self.suit in ['♥', '♦']:
            return f"{white_bg}{red_col}| {self.suit}{val} |{reset}"

        # handle black colors for Clubs and Spades
        else: 
            return f"{white_bg}{black_col}| {self.suit}{val} |{reset}"
        
        

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print(card.show())
        
    # Generate 52 cards
    def build(self):
        self.cards = []

        for suit in suits:
            for val in range(1,14):
                self.cards.append(Card(suits[suit], val))

    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
            # You can also use the build in shuffle method
            # random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()
    
    def cards_left(self): 
        return len(self.cards)

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0 
        self.aces = 0
        # self.hand = Hand()
        self.chips = Chips().total

    def sayHello(self):
        print(f"Hi! My name is {self.name}")
        # return self
    
    def countChips(self): 
        print(f"Chip count is: {self.chips}")
        # return self

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                # for display purposes, build list of cards 
                self.hand.append(card)
                # handle various card values to track the hand's score
                if card.value == 14:  # handle Aces 
                    self.aces += 1 
                    self.score += 11
                elif card.value >= 10: # handle face cards and 10 card 
                    self.score += 10
                else:
                    self.score += card.value
            else: 
                return False
        return True

    def discard(self):
        return self.hand.pop()
    
    def adjust_for_ace(self):
        if self.score > 21 and self.aces > 1: 
            self.score -= 10 
            self.aces -= 1     
        
    # Display all the cards in the players hand
    def showHand(self):
        print(f"{self.name}'s hand: {self.hand}")
        return self.hand

    # Return score for the player's hand 
    def scoreHand(self): 
        print(f"{self.name} has {self.score} points.")   
        
    # Run showHand and scoreHand methods 
    def status(self):
        self.showHand()
        self.scoreHand()
        print("\n")
    
class Chips(object):
    """
    Player count of chips. All players start with 200
    """
    def __init__(self):
        self.total = 200
        self.bet = 0    

    def win_bet(self): 
        self.total +- self.bet 
        
    def lose_bet(self):
        self.total -= self.bet 

# Function definitions 

def take_bet(chips):
    while True:
        
        chips.bet = input("How many chips would you like to bet : ")
        
        # Hidden menu item to quit
        if chips.bet[0] == 'q':
            sys.exit("Quiting Blackjack.py")
        else:
            try:
                chips.bet = int(chips.bet)
            
            except ValueError:
                print("Oops!, Bet must be an integer! Enter an integer")
            else:
                if chips.bet > chips.total:
                    print("Sorry, you don't have enough chips")
                # Hidden menu item to quit program 
                
                else:
                    break
            
def hit(deck, player):
    player.draw(deck, 1)
    player.adjust_for_ace()

def hit_or_stand(deck, player):
    global playing
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' : ")
        
        if x[0].lower() == 'h':
            hit(deck, player)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        
        # Hidden menu option to quit game 
        elif x[0].lower() == 'q':
            sys.exit("Quitting Blackjack.py") 

        else:
            print("Sorry, please try again.")
            continue
        break            

            
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


####  Begin initial game setup 

print('***Welcome to BlackJack!***\n\nGet as close to 21 as you can without going over!\nDealer hits until he reaches 17. Aces count as 1 or 11.\n')

deck = Deck()
deck.shuffle()


player = Player("Joe")

player_chips = Chips()
player.countChips()

dealer = Player("Dealer")

# MAIN GAME LOOP 
while True: 

    take_bet(player_chips)

    player.draw(deck, 2)
    player.status()

    dealer.draw(deck, 2) 
    dealer.status()
    
    while playing: 
        
        # Prompt player to hit or stand 
        hit_or_stand(deck, player)
        player.status()
        dealer.status()
    
    # If player over 21, then busts 
    if player.score > 21:
        player_busts(player, dealer, player_chips)
        break     
   
    # If player has not busted, play Dealer's hand 
    if player.score <= 21:
        
        while dealer.score < 17:
            hit(deck,dealer)
            
              
            # Test different winning scenarios
            if dealer.score > 21:
                dealer_busts(player,dealer,player_chips)
                dealer.status()

            elif dealer.score > player.score:
                dealer_wins(player,dealer,player_chips)
                dealer.status()

            elif dealer.score < player.score:
                player_wins(player,dealer,player_chips)

            else:
                push(player,dealer)

    # Inform Player of their chips total    
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' :  ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
    