# A card will have a suit and value (from 1 - 10)

class Card:

    def __init__(self, suit, value):
        self._suit = suit # protected: only accessible by the class and derived classes
        self._value = value # protected

    def getSuit(self):
        return self._suit
    
    def getValue(self):
        return self._value
    
    def print(self):
        print(self.getSuit(), self.getValue())