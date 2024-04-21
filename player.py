# A player has a hand of cards
# A player will make a move in each round
# We have two different kinds of player: Dealer and UserPlayer
# Abstract Base Class (ABC): does not have definition on its own and has abstract methods which forces the implementation in its derived classes
# and it's not allowed to instantiate objects for a abstract base class

from abc import ABC, abstractmethod
from hand import Hand

class Player(ABC):

    def __init__(self, hand):
        self._hand = hand

    def showHand(self):
        return self._hand
    
    def clearHand(self):
        self._hand = Hand()

    def addCard(self, card):
        self._hand.addCard(card)

    @abstractmethod
    def makeMove(self):
        pass # will be overridden by subclasses


# A UserPlayer will have a balance and be able to place a bet
# Override makeMove(): True to draw a card and False to stop


class UserPlayer(Player): # child class of Player
    def __init__(self, balance, hand):
        super().__init__(hand) # access to the methods of the base class
        self._balance = balance

    def getBalance(self):
        return self._balance

    def placeBet(self, amount):
        if amount > self._balance:
            raise ValueError('Not enough money to place!')
        self._balance -= amount
        return amount

    def receiveBet(self, amount):
        self._balance += amount

    def makeMove(self):
        if self.showHand().getScore() > 21:
            return False
        move = input('Draw card? [y/n] ')
        return move == 'y'

# A Dealer will draw until their hand value is greater than or equal to the player's hand value


class Dealer(Player): # child class of Player
    def __init__(self, hand):
        super().__init__(hand) # access to the methods of the base class
        self._targetScore = 17 # random default value

    def updateTargetScore(self, score):
        self._targetScore = score # update after the player draws

    def makeMove(self):
        return self.getHand().getScore() < self._targetScore




    