#!python3

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

class FrenchDeck:
    """ General class structure for French card deck. """
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        """ Special method for class initialization. """
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        """ Special method for getting deck length. """
        return len(self._cards)

    def __getitem__(self, position):
        """ Special method for getting specific card in deck. """
        return self._cards[position]

def spades_high(card):
    """ Returns score between [0, 52] for card value. """
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

def main(deck):
    """ Main run function. """
    # Simple card representation
    """
    beer_card = Card("7", "diamonds")
    print(beer_card)
    """

    # Simple deck representation
    """
    print(len(deck))
    """

    # Read specific card from deck by index using __getitem__
    """
    print(deck[0])
    print(deck[-1])
    """

    # Grab random choice from deck using random library
    """
    from random import choice
    print(choice(deck))
    """

    # Slicing on deck using __getitem__
    """
    print(deck[:3])
    print(deck[12::13])
    """

    # Iterating over deck using __getitem__
    """
    for card in deck:
        print(card)
    """

    # Iterating over deck in reverse using __getitem__
    """
    for card in reversed(deck):
        print(card)
    """

    # Sequential scan by iteration is possible
    """
    print(Card("Q", "hearts") in deck)
    print(Card("7", "beasts") in deck)
    """

    # List our deck in increasing rank order
    for card in sorted(deck, key=spades_high):
        print(card)

if __name__ == "__main__":
    deck = FrenchDeck()
    main(deck)