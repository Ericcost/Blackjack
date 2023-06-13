import random 

class Card: 
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"
    

class Deck: 

    def __init__(self):
        self.cards = []

        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "K", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "10", "value": 10},
            {"rank": "9", "value": 9},
            {"rank": "8", "value": 8},
            {"rank": "7", "value": 7},
            {"rank": "6", "value": 6},
            {"rank": "5", "value": 5},
            {"rank": "4", "value": 4},
            {"rank": "3", "value": 3},
            {"rank": "2", "value": 2},
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
                
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
        else: 
            print("One card left, no need to shuffle")

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0: 
                card = self.cards.pop()
                cards_dealt.append(card)
            else:
                print("No cards left")

        return cards_dealt

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer 
    
    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0 
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank['value'])
            self.value += card_value
            if card.rank['value'] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10
        # return self.value
    
    def get_value(self):
        self.calculate_value()
        return self.value
    
    def  is_blackjack(self):
        return self.get_value() == 21
    
    def display(self):
        print(f''' {"Dealer's" if self.dealer else "Your"} hand:  ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer:
                print('hidden')
            else: 
                print(card)

        if not self.dealer:
            print(f"Value: {self.get_value()}")
        


deck = Deck()
deck.shuffle()

hand = Hand()
hand.add_card(deck.deal(2))

hand.display()