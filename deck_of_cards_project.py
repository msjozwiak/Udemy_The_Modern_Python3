from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        # return f"{self.value} of {self.suit}"
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def __repr__(self):
        # return f"Deck of {self.suit}"
        return "Deck of {} cards".format(self.count())

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        count = self.count()
        actual = min(count, number)
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle_deck(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self


# d = Deck()
# print(d.shuffle_deck())
# card1 = d.deal_card()
# print(card1)
# hand = d.deal_hand(5)
# print(hand)
# print(d.cards)
my_deck = Deck()
my_deck.shuffle_deck()
for card in my_deck:
    print(card)
