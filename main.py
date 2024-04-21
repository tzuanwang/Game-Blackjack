from player import Dealer, UserPlayer
from hand import Hand
from gameround import GameRound
from deck import Deck


player = UserPlayer(1000, Hand())
dealer = Dealer(Hand())

while player.getBalance() > 0:
    gameRound = GameRound(player, dealer, Deck()).play()
