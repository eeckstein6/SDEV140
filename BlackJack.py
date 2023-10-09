import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if rank in ['J', 'Q', 'K']:
            self.value = 10
        elif rank == 'A':
            self.value = 11
        else:
            self.value = int(rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    def __init__(self):

        self.cards = []
        for suit in ['H', 'D', 'C', 'S']:
            for rank in range(2, 11):
                self.cards.append(Card(suit, str(rank)))
            for rank in ['J', 'Q', 'K', 'A']:
                self.cards.append(Card(suit, rank))

    def shuffle(self):

        random.shuffle(self.cards)

    def deal_card(self):

        return self.cards.pop()


class Hand:
    def __init__(self):

        self.cards = []
        self.value = 0

    def add_card(self, card):

        self.cards.append(card)
        self.value += card.value
        if self.value > 21 and any(card.rank == 'A' for card in self.cards):
            self.value -= 10

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def play(self):
        print("Welcome to Blackjack!")
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        print(f"Your hand: {self.player_hand}")
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        print(f"Dealer's hand: {self.dealer_hand.cards[0]}")
        while True:
            choice = input("Hit or stand? ").lower()
            if choice == 'hit':
                self.player_hand.add_card(self.deck.deal_card())
                print(f"Your hand: {self.player_hand}")
                if self.player_hand.value > 21:
                    print("You bust!")
                    return
            elif choice == 'stand':
                break
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
        print(f"Dealer's hand: {self.dealer_hand}")
        if self.dealer_hand.value > 21:
            print("Dealer busts! You win!")
        elif self.dealer_hand.value > self.player_hand.value:
            print("Dealer wins!")
        elif self.player_hand.value > self.dealer_hand.value:
            print("You win!")
        else:
            print("It's a tie!")
            
game = Game()
game.play()