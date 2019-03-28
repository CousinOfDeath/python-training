import random
from termcolor import colored, cprint

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


class NoMoreCards(Exception):

    def __init__(self):
        super(NoMoreCards, self).__init__("No more cards left.")


class NoMoreBalance(Exception):

    def __init__(self):
        super(NoMoreBalance, self).__init__("No more cbalance.")


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
        self.cards = []

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def busted(self):
        return self.get_value() > 21

    def get_value(self):
        """
        First count ace as 1,
        after counting the rest
        check if adding 10 doesnt
        go over 21
        """
        value = 0
        has_ace = False
        for card in self.cards:
            rank = card.get_rank()
            if rank == 'A':
                has_ace = True
            value += VALUES[rank]
        if value < 12 and has_ace:
            return value + 10
        return value


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

        # Deal random
        # card = self.cards[random.randint(0, cards_left - 1)]

        try:
            # Deal from the top
            card = self.cards[cards_left - 1]
            self.cards.remove(card)
            return card
        except IndexError:
            raise NoMoreCards()


class Table:
    def __init__(self, max_players):
        self.dealer = Player("Dealer", 0, True)
        self.players = []
        self.max_players = max_players
        self.deck = Deck()

    def add_player(self, player):
        # Todo if table has room
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def has_players(self):
        return len(self.players) > 0


class Player:
    def __init__(self, name, balance, dealer):
        self.name = name
        self.balance = balance
        self.hand = Hand()
        self.dealer = dealer

    def add_balance(self, amount):
        self.balance += amount

    def decrease_balance(self, amount):
        if self.balance < amount:
            raise NoMoreBalance()
        else:
            self.balance -= amount

    def __str__(self):
        if self.dealer:
            return f"{self.name}: Hand: {self.hand}, value: {self.hand.get_value()}"
        else:
            return f"{self.name}: balance: {self.balance}. Hand: {self.hand}, value: {self.hand.get_value()}"


def play():
    start = False
    count = 1
    table = Table(5)

    while start is False:
        print(F"Enter name for player {count}. You will be given 10 credits to play.")
        name = input()
        # TODO: Validate length and uniqueness
        player = Player(name, 10, False)
        table.add_player(player)

        print("Wanna start or are there more players? Insert 'Y' to start and some other key to add another player.")
        # TODO: Validate input
        start = input() is 'y'
        count += 1

        if start:
            break

    while table.has_players():

        # When to shuffle and add new deck?
        table.deck = Deck()
        table.deck.shuffle()

        # Deduct balance
        for player in table.players:
            player.decrease_balance(1)

        # Deal two cards for dealer
        table.dealer.hand = Hand()
        table.dealer.hand.add_card(table.deck.deal_card())
        table.dealer.hand.add_card(table.deck.deal_card())
        print(table.dealer)

        # Deal two cards for players
        for player in table.players:
            player.hand = Hand()
            player.hand.add_card(table.deck.deal_card())
            player.hand.add_card(table.deck.deal_card())
            cprint(player, "green")

        # Check whether the players want more cards
        for player in table.players:
            move_on = False
            print(f"{player.name}: Card 'y/n'?")

            # TODO: Validate input
            hit_me = input() is 'y'

            if hit_me:
                while hit_me:
                    # Deal card
                    player.hand.add_card(table.deck.deal_card())
                    cprint(player, "yellow")

                    # Check if busted
                    if player.hand.busted():
                        cprint("Sorry you busted", "red")
                        move_on = True
                        break
                    else:
                        print(f"{player.name}: Card 'y/n'?")
                        hit_me = input() is 'y'
            else:
                move_on = True

            # To next player
            if move_on:
                continue

        # Players that did not bust
        not_busted = [p for p in table.players if not p.hand.busted()]

        # Dealer taking cards
        while len(not_busted) > 0 and table.dealer.hand.get_value() < max(p.hand.get_value() for p in not_busted):
            table.dealer.hand.add_card(table.deck.deal_card())
            print(table.dealer)

        if table.dealer.hand.busted():
            cprint("Dealer busted", "red")

            # If dealer busted then all not busted players win
            for player in not_busted:
                player.add_balance(2)
                cprint(player, "green")
        else:
            # TODO: Get the winner(s)
            # greater_than_dealer = [p for p in not_busted if p.hand.get_value() > table.dealer.hand.get_value()]
            #for player in greater_than_dealer:
            #    player.add_balance(2)
            #    cprint(player, "green")
            d = 0



#d = Deck()

#counter = 1
#while counter <= 52:
#    print(d.deal_card())
#    counter += 1

play()