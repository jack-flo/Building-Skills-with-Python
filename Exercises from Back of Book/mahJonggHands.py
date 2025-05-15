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
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit.lower()

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


class TileSet(object):
    def __init__(self):
        self.tiles = []

    def __str__(self):
        return '[' + ', '.join(str(t) for t in self.tiles) + ']'

    def canContain(self, aTile):
        if not self.tiles:
            return True
        elif self.full():
            return False
        else:
            return aTile == self.tiles[-1]

    def full(self):
        return NotImplemented

    def pair(self):
        return False  # need to override for pair class

    def add(self, aTile):
        self.tiles.append(aTile)

    def fallback(self, tileStack):
        for t in reversed(self.tiles):
            tileStack.insert(0, t)
        # return an instance of the subclass that called the method
        return type(self)()


class PairSet(TileSet):
    def full(self):
        return len(self.tiles) == 2

    def pair(self):
        return True

    def fallback(self, tileStack):
        for t in reversed(self.tiles):
            tileStack.insert(0, t)
        return None


class ThreeSet(TileSet):
    def full(self):
        return len(self.tiles) == 3

    def fallback(self, tileStack):
        for t in reversed(self.tiles):
            tileStack.insert(0, t)
        return SequenceSet()


class FourSet(TileSet):
    def full(self):
        return len(self.tiles) == 4

    def fallback(self, tileStack):
        for t in reversed(self.tiles):
            tileStack.insert(0, t)
        return ThreeSet()


class SequenceSet(TileSet):
    """Holds 3 tiles of the same suit which must have an ascending rank"""

    def full(self):
        return len(self.tiles) == 3

    def canContain(self, aTile):
        if not self.tiles:
            return True

        if self.full():
            return False

        last = self.tiles[-1]
        # check that is a suitTile
        if not isinstance(aTile, SuitTile):
            return False
        # check is the same suit
        if aTile.getSuit() != self.tiles[0].getSuit():
            return False
        # check ascending order
        return aTile.getRank() == last.getRank() + 1

    def fallback(self, tileStack):
        for t in reversed(self.tiles):
            tileStack.insert(0, t)
        return PairSet()


class Hand(object):
    def __init__(self, *tiles):
        self.tiles = list(tiles)
        self.sets = []

    def sortTiles(self):
        suitOrder = {'dot': 0, 'bamboo': 1, 'wan': 2}
        # create a key for the sort() function

        def tileKey(tile):
            suit = tile.getSuit()
            if suit is None:
                # then tile is honour
                return (1, 0, 0, tile.getName())
            else:
                # suit tiles sort by (0, suitOrder, rank, name)
                return (0,
                        suitOrder[suit],
                        tile.getRank(),
                        tile.getName())
        self.tiles.sort(key=tileKey)

    def examine(self, tileStack, setStack):
        while tileStack:
            t = tileStack.pop(0)
            currentSet = setStack[-1]

            if currentSet.full():
                setStack.append(FourSet())
                # place back if the in the tileStack
                tileStack.insert(0, t)
                continue

            if currentSet.canContain(t):
                currentSet.add(t)
            else:
                tileStack.insert(0, t)
                return
        return None

    def retry(self, tileStack, setStack):
        while setStack:
            s = setStack.pop()
            nextSet = s.fallback(tileStack)
            if nextSet:
                return nextSet
        return None

    def allFull(self, setStack):
        if len(setStack) != 5:
            return False
        for s in setStack:
            if not s.full():
                return False

        pairCount = 0
        for s in setStack:
            if s.pair():
                pairCount += 1
        if pairCount != 1:
            return False

        return True

    def mahjongg(self):
        self.sortTiles()
        setStack = [FourSet()]
        tileStack = list(self.tiles)
        self.examine(tileStack, setStack)

        while not self.allFull(setStack):
            newSet = self.retry(tileStack, setStack)
            if newSet is None:
                return False

            setStack.append(newSet)
            self.examine(tileStack, setStack)
        self.sets = setStack
        return True

    def points(self):
        pass

    def totalDoubles(self):
        pass

    def finalScore(self):
        pass


def testHand1():
    t1 = [SuitTile(2, "Bamboo"), SuitTile(2, "Bamboo"),
          SuitTile(2, "Bamboo"), SuitTile(3, "Bamboo"),
          SuitTile(4, "Bamboo"), SuitTile(5, "Bamboo"),
          SuitTile(5, "Bamboo"), SuitTile(5, "Bamboo"),
          SuitTile(2, "Dot"), SuitTile(2, "Dot"),
          SuitTile(2, "Dot"), HonourTile("Green"),
          HonourTile("Green"), HonourTile("Green"), ]
    h1 = Hand(*t1)
    print(h1.mahjongg())


if __name__ == '__main__':
    print('Starting Test')
    testHand1()
    print('Finished')
