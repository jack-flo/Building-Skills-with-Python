from functools import total_ordering
import random

# A game is played with a deck of tiles.
# there are three suits (dots, bamboo, and wan) and each is ranked 1-9
# There are honours too; four winds (NSEW), and three dragons (WRG)

# Define a parent class of Tile, and two subclasses, SuitTile and HonorTile
# SuitTile has a suit and rank, HonourTile has only a name


class Tile(object):

    suitOrder = {'dot': 0, 'bamboo': 1, 'wan': 2}

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.getName()

    def __eq__(self, other):
        return self.getName() == other.getName()

    def __ne__(self, other):
        return self.getName() != other.getName()

    def getSuit(self):
        return NotImplemented

    def getRank(self):
        return NotImplemented

    def getName(self):
        return self.name


@total_ordering
class SuitTile(Tile):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def getName(self):
        name = self.suit + str(self.rank)
        return name

    def __lt__(self, other):
        # compare suits
        if self.suitOrder[self.suit] != self.suitOrder[other.suit]:
            return self.suitOrder[self.suit] < self.suitOrder[other.suit]
        return self.rank < other.rank

    def __eq__(self, other):
        return (self.suit, self.rank) == (other.suit, other.rank)


class HonourTile(Tile):
    def getSuit(self):
        return None

    def getRank(self):
        return None

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return HonourTile.__eq__()

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        return HonourTile.__eq__()


class Wall(object):
    def __init__(self):
        self.set = []
        for suit in ['dot', 'bamboo', 'wan']:
            for n in range(1, 10):
                self.set.append((suit, n))
        for honour in ['east', 'south', 'west', 'north', 'red', 'white', 'green']:
            self.set.append(honour)

    def __str__(self):
        return f"{self.set}"

    def shuffle(self):
        return random.shuffle(self.set)

    def deal(self):
        """Creates a generator object that will have to be assigned during gameplay and then cycled through using next()"""
        for card in self.set:
            yield card


wall = Wall()
wall.shuffle()
wallDealer = wall.deal()
print(next(wallDealer))
