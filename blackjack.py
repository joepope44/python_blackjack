import random 

class Card(object): 
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value 

    def __repr__(self): 
        return f"{self.value} of {self.suit}"

class Deck(object):
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamnods"] for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]

    def shuffle(self): 
        if len(self.cards) > 1: 
            random.shuffle(self.cards) 

    def deal(self): 
        if len(self.cards) > 1: 
            return self.cards.pop(0)

class Hand(object):
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card) 

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else: 
                if card.value == "A":
                    has_ace = True
                    self.value += 11 
                else:
                    self.value += 10 

        if has_ace and self.value > 21: 
            self.value -= 10 
        
    def get_value(self):
        self.calculate_value()
        return self.value 

    def display(self):
        if self.dealer:
            print("hidden")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Value:". self.get_value())

class Game: 
    def __init__(self):
        pass
    
    def play(self):
        playing = True

        while playing: 
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand() 
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal()) 
            
            print("Your hand is:")
            self.player_hand.display()
            print()
            print("Dealer's hand is:")
            self.dealer_hand.display()







card1 = Card("Clubs", "6")
card2 = Card("Hearts", "K")
print(card1, "\n", card2)