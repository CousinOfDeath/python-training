import random

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J':10,
    'Q':10,
    'K':10
}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"Suit: {self.suit} and rank: {self.rank}"

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank



class Hand:
    def __init__(self):
        """
        create a list to store the cards in
        """

    def __str__(self):
        pass

    def add_card(self, card):
        pass

    def get_value(self):
        """
        First count ace as 1,
        after counting the rest
        check if adding 10 doesnt
        go over 21
        """
        pass


class Deck:
    def __init__(self):
        """
        store all cards in a deck
        """
        self.cards = []

        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        cards_left = len(self.cards)
        # print(f"Cards left: {cards_left}")
        # Deal random
        # card = self.cards[random.randint(0, cards_left - 1)]
        # Deal from the top
        card = self.cards[cards_left - 1]

        self.cards.remove(card)

        return card


d = Deck()


counter = 1
while counter <= 52:
    print(d.deal_card())
    counter += 1