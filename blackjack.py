import random
from colorama import init, Fore, Back, Style
init()


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
        for suit in ['♥', '♣', '♦', '♠']:
            for val in range(1,14):
                self.cards.append(Card(suit, val))

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

    def sayHello(self):
        print(f"Hi! My name is {self.name}")
        return self

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else: 
                return False
        return True
    
    def scoreHand(self):
        hand_score = 0
        for card in self.hand:
            
            # handle Ace
            if card.value == 14: 
                #TODO: handle user input for 1 or 11 
                hand_score += 11
            # if card.value is J, Q, K         
            if card.value > 10:
                hand_score += 10 
            else:
                hand_score += card.value
        print(f"Hand score: {hand_score}")

    # Display all the cards in the players hand
    def showHand(self):
        print(f"{self.name}'s hand: {self.hand}")
        return self

    def discard(self):
        return self.hand.pop()

# Test making a Card
# card = Card('Spades', 6)
# print(card)

# Test making a Deck
myDeck = Deck()
myDeck.shuffle()
# deck.show()

player = Player("Joe")
player.sayHello()
player.draw(myDeck, 2)
player.showHand()
player.scoreHand()
myDeck.cards_left()
