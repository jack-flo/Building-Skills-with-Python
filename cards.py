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

    def getHardValue(self):
        if self.rank > 10:
            return 10
        else:
            return self.rank

    def getSoftValue(self):
        if self.rank > 10:
            return 10
        elif self.rank == 1:
            return 11
        else:
            return self.rank


class Hand (object):
    """The Hand has a collection of cards in a sequence"""

    def __init__(self, *cards):
        self.cards = list(cards)

    def __str__(self):
        hand = ",".join(map(str, self.cards))
        return hand

    def hardTotal(self):
        total = 0
        for card in self.cards:
            total += card.getHardValue()
        return total

    def softTotal(self):
        total = 0
        aceFound = False
        for card in self.cards:
            if not aceFound and card.rank == 1:
                total += card.getSoftValue()
                aceFound = True
            else:
                total += card.getHardValue()
        return total

    def add(self, card):
        self.cards.append(card)


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

# Generated code because I got bored of blackjack


def main():
    # 1. build deck + deal initial cards
    deck = Deck()
    deck_gen = deck.deal()

    player = Hand(next(deck_gen), next(deck_gen))
    dealer = Hand(next(deck_gen), next(deck_gen))

    # 2. player hits until hard ≥ 21
    while player.hardTotal() < 21:
        player.add(next(deck_gen))

    # 3. dealer hits by the “soft 16 or less” rule
    while True:
        soft = dealer.softTotal()
        hard = dealer.hardTotal()

        if soft <= 16 or (soft > 21 and hard <= 16):
            dealer.add(next(deck_gen))
        else:
            break

    # 4. show results
    print("Player’s final hand:", player)
    print(" Player hard total:", player.hardTotal(),
          "soft total:", player.softTotal())
    print("Dealer’s final hand:", dealer)
    print(" Dealer hard total:", dealer.hardTotal(),
          "soft total:", dealer.softTotal())


main()
