import random
import os
import time

class Card:
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = {'C': '♣', 'D': '♦', 'H': '♥', 'S': '♠'}
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    def is_ace(self):
        return self.rank == 'A'

    def is_face_card(self):
        return self.rank in {'J', 'Q', 'K'}

class Deck:
    def __init__(self):
        self.reset()

    def reset(self):
        self.cards = [Card(rank, suit) 
                      for rank in Card.RANKS
                      for suit in Card.SUITS]
        random.shuffle(self.cards)
    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, cards):
        self._cards = cards

    def is_empty(self):
        return len(self.cards) == 0
    
    def draw(self):
        return self.cards.pop()

class Participant:
    def __init__(self):
        self._hand = []
        self.busted = False

    # balance??
    def hit(self, card):
        self.hand.append(card)

    def stay(self):
        print(f'You chose to stay at {self.score}')
        time.sleep(1)

    def is_busted(self):
        if self.score > 21:
            self.busted = True
            return True
        return False
    
    @property
    def busted(self):
        return self._busted
    
    @busted.setter
    def busted(self, busted):
        self._busted = busted

    @property
    def hand(self):
        return self._hand

    @property
    def score(self):
        return self.hand_value()

    def hand_value(self):
        total = 0
        aces = 0
        for card in self.hand:
            if card.is_ace():
                aces += 1
                total += 11
            elif card.is_face_card():
                total += 10
            else:
                total += int(card.rank)
        while total > 21 and aces:
            total -= 10
            aces -= 1
        
        return total


class Player(Participant):
    def __init__(self):
        super().__init__()
        self.balance = 0
        

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self.deck = Deck()
        self._hide = True

    @property
    def hide(self):
        return self._hide

    def reveal(self):
        self._hide = False

    def deal(self):
        if self.deck.is_empty():
            self.deck.reset()
        return self.deck.draw()

class TwentyOneGame:
    WIN_CON = 21
    DEALER_LIMIT = 17 

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        self.display_welcome_message()
        self.deal_cards()
        if self.check_natural():
            if self.dealer.score == TwentyOneGame.WIN_CON:
                self.dealer.reveal()
            self.show_cards()
            self.display_result()
            return
        self.show_cards()
        self.player_turn()
        if self.player.busted:
            self.show_cards()
            self.display_result()
            return
        self.dealer_turn()
        if self.dealer.busted:
            self.show_cards()
            self.display_result()
            return 
        self.display_result()
        self.display_goodbye_message()

    def deal_cards(self):
        self.player.hit(self.dealer.deal())
        self.dealer.hit(self.dealer.deal())
        self.player.hit(self.dealer.deal())
        self.dealer.hit(self.dealer.deal())

    def check_natural(self):
        player_natural = self.player.score == TwentyOneGame.WIN_CON
        dealer_natural = self.dealer.score == TwentyOneGame.WIN_CON
        return player_natural or dealer_natural


    def show_cards(self):
        os.system('clear')
        dealer_hand = self.dealer.hand
        player_hand = self.player.hand
        
        if self.dealer.hide:
            suit = Card.SUITS[dealer_hand[0].suit]
            rank = dealer_hand[0].rank

            dealerline1 = f'|          {suit}|  |'
            dealerline2 = f'|_________{rank.rjust(2,'_')}|__|'
        else:
            dealerline1 = '|        '
            dealerline2 = '|________'

            for card in dealer_hand:
                suit = Card.SUITS[card.suit]
                rank = card.rank
                dealerline1 += f' {suit}|'
                dealerline2 += f'{rank.rjust(2,'_')}|'
        
        line1 = ''
        line2 = '|'
        line3 = '|'
        for i, card in enumerate(player_hand):
            rank = card.rank.ljust(2)
            suit = Card.SUITS[card.suit]

            if i == len(player_hand) - 1:
                line1 += '_' * 11
                line2 += rank + ' ' * 8 + '|'
                line3 += suit + ' ' * 8 + ' |'
            else:
                line1 += '_' * 3
                line2 += rank + '|'
                line3 += suit + ' |'
        
        print(dealerline1)
        print(dealerline2)
        print()
        print(line1)
        print(line2)
        print(line3)

    def player_turn(self):
        while True:
            if self.player.score == TwentyOneGame.WIN_CON:
                print("You hit 21! Dealers turn...")
                time.sleep(1)
                break
            choice = self.player_choice()
            if choice == 'h':
                self.player.hit(self.dealer.deal())
            if choice == 's':
                self.player.stay()
                break
            if self.player.is_busted():
                break
            self.show_cards()

    def player_choice(self):
        while True:
            choice = input("hit or stay? (h/s)").strip().lower()
            if choice in {'h', 's'}:
                return choice
            print("Sorry, must enter 'h' or 's'.")

    def dealer_turn(self):
        self.dealer.reveal()
        self.show_cards()
        time.sleep(1)

        while self.dealer.score < 17:
            self.dealer.hit(self.dealer.deal())
            self.show_cards()
            time.sleep(0.5)
        if self.dealer.is_busted():
            return
        print(f"Dealer stays at {self.dealer.score}")

    def display_welcome_message(self):
        print("Welcome to 21!")

    def display_goodbye_message(self):
        print("Thank you for playing 21!")

    def display_result(self):
        if self.player.busted:
            print("You busted, dealer wins!")
            return
        if self.dealer.busted:
            print("Dealer busted, you win!")
            return

        player_total = self.player.score
        dealer_total = self.dealer.score
        if player_total > dealer_total:
            print("You win!")
            return
        elif player_total < dealer_total:
            print("Dealer wins!")
            return
        else:
            print("You tied!")
            return


game = TwentyOneGame()
game.start()