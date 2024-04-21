# A hand will contain an array of cards and its total value
# When we add a card, we recalculate the total value
# Remember to add the logic of Ace: either 1 or 11 whichever is best for the player

class Hand:

    def __init__(self):
        self._score = 0
        self._cards = []

    def addCard(self, card):
        self._cards.append(card)
        if card.getValue() != 1:
            self._score += card.getValue()
        else:
            if (self._score + 11) > 21:
                self._score += 1
            else:
                self._score += 11

    def getScore(self):
        return self._score
    
    def getCards(self):
        return self._cards
    
    def print(self):
        for card in self._cards:
            print(card.getSuit(), card.getValue())