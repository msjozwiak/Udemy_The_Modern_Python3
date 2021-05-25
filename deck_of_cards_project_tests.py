import unittest
from deck_of_cards_project import Card, Deck
from copy import deepcopy


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "Hearts")

    def test_init(self):
        """cards should have suits and a value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """repr should return a string of the form 'VALUE of SUIT"""
        self.assertEqual(self.card.__repr__(), "A of Hearts")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """decks should have a cards attribute, which is a list"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr_full_deck(self):
        """repr should return a string of the form 'Deck of 52 cards"""
        self.assertEqual(self.deck.__repr__(), "Deck of 52 cards")

    def test_count_full_deck(self):
        self.assertEqual(self.deck.count(), 52)

    def test_count_half_deck(self):
        self.deck.deal_hand(26)
        self.assertEqual(self.deck.count(), 26)

    def test_count_empty_deck(self):
        self.deck.deal_hand(52)
        self.assertEqual(self.deck.count(), 0)

    def test_count_illegal_number(self):
        self.deck.deal_hand(100)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_sufficient_cards(self):
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        """deal_card should deal a single card from the deck"""
        self.assertEqual(self.deck.cards[-1], self.deck.deal_card())

    def test_deal_hand(self):
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        deck1 = deepcopy(self.deck)
        self.deck.shuffle_deck()
        self.assertNotEqual(deck1.cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle_deck()


if __name__ == "__main__":
    unittest.main()
