# Build up the deck: 13 cards for each suit
# Draw cards each round
# Shuffle the cards
import random
from suit import Suit
from card import Card

class Deck:

    # Build up the deck
    def __init__(self):
        self._cards = []
        for suit in Suit: # 4 suits
            for val in range(1, 14): # 13 cards
                self._cards.append(Card(suit, min(val, 10))) # 1-9 and 10 * 3

    def print(self):
        for card in self._cards:
            card.print()

    def draw(self):
        return self._cards.pop()
    
    def shuffle(self):
        for i in range(len(self._cards)): # iterate over all cards
            j = random.randint(0, 51) # randomly pick a number between 1 - 52 (position)
            self._cards[i], self._cards[j] = self._cards[j], self._cards[i] # exchange the position