from functools import total_ordering
import random


@total_ordering  # means you only have to supply __eq__ and another dunder for it to complete the rest
class Card (object):
    """Functions for cards"""

    def __init__(self, rank, suit):
        # Rank 1 to 13, suits C, D, H, S
        self.rank = rank
        self.suit = suit

    def __str__(self):
        convertedNumber = self.rank
        # Create a pretty string of the card
        if self.rank == 1:
            convertedNumber = 'A'
        elif self.rank == 11:
            convertedNumber = 'J'
        elif self.rank == 12:
            convertedNumber = 'Q'
        elif self.rank == 13:
            convertedNumber = 'K'

        return f"{convertedNumber}{self.suit}"

    # def __eq__(self, other):
    #     if self.rank == other.rank and self.suit == other.suit:
    #         return True
    #     else:
    #         return False

    def __eq__(self, other):
        return (self.rank, self.suit) == (other.rank, other.suit)

    def __ne__(self, other):
        if self.rank != other.rank and self.suit != other.suit:
            return True
        else:
            return False

    # def __lt__(self,other):
    #     if self.rank == other.rank:
    #         if self.suit < other.suit:
    #             return True
    #         else:
    #             False
    #     else:
    #         if self.rank < other.rank:
    #             return True
    #         else:
    #             return False

    def __lt__(self, other):
        return (self.rank, self.suit) < (other.rank, other.suit)


class Deck(object):
    """Cards are dealt from a deck, which holds dealing methods"""

    def __init__(self):
        # create the deck
        self.deck = []
        for suit in ['C', 'D', 'H', 'S']:
            for rank in range(1, 14):
                card = Card(rank, suit)
                self.deck.append(card)

    def deal(self):
        # shuffle cards and deal
        random.shuffle(self.deck)
        for card in self.deck:
            yield card
