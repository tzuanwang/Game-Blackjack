class GameRound:
    def __init__(self, player, dealer, deck):
        self._player = player
        self._dealer = dealer
        self._deck = deck

    def getBetUser(self):
        amount = int(input('Enter a bet amount: '))
        return amount

    def dealInitialCards(self):
        for i in range(2):
            self._player.addCard(self._deck.draw())
            self._dealer.addCard(self._deck.draw())
        print('Player hand: ')
        self._player.showHand().print()
        dealerCard = self._dealer.showHand().getCards()[0]
        print("Dealer's first card: ")
        dealerCard.print()

    def cleanupRound(self):
        self._player.clearHand()
        self._dealer.clearHand()
        print('Player balance: ', self._player.getBalance())

    def play(self):
        self._deck.shuffle()

        if self._player.getBalance() <= 0:
            print('Player has no more money =)')
            return
        userBet = self.getBetUser()
        self._player.placeBet(userBet)

        self.dealInitialCards()

        # User makes moves
        while self._player.makeMove():
            drawnCard = self._deck.draw()
            print('Player draws', drawnCard.getSuit(), drawnCard.getValue())
            self._player.addCard(drawnCard)
            print('Player score: ', self._player.showHand().getScore())

        if self._player.showHand().getScore() > 21:
            print('Player 💥')
            self.cleanupRound()
            return
        
        # Dealer makes moves
        while self._dealer.makeMove():
            self._dealer.addCard(self._deck.draw())
        
        # Determine winner
        if self._dealer.showHand().getScore() > 21:
            print('Player wins')
            self._player.receiveBet(userBet * 2)
        elif self._dealer.showHand().getScore() > self._player.showHand().getScore():
            print('Player loses')
        else:
            print('Game ends in a draw')
            self._player.receiveBet(userBet)
        self.cleanupRound()
