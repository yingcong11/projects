#Global variables
import random
suits = ("Hearts", "Diamond", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
          "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7,
          "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

#classes
class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #create card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        single_card = self.all_cards.pop()
        return single_card

class Player():

    def __init__(self, name, capital):
        self.name = name
        self.capital = capital
        self.hand = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        playerhand = ""
        for card in self.hand:
            playerhand += "\n"+card.__str__()
        return playerhand

    def lose_bet(self, amt):
        amt = int(amt)
        self.capital -= amt

    def win_bet(self, amt):
        amt = int(amt)
        self.capital += amt

    def draw_one(self, new_card):
        self.hand.append(new_card)
        self.value += values[new_card.rank]
        if new_card.rank == "Ace":
            self.aces += 1
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
        return self.hand

class Dealer():
    
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        dealerhand = ""
        for card in self.hand:
            dealerhand += "\n"+card.__str__()
        return dealerhand

    def draw_one(self, new_card):
        self.hand.append(new_card)
        self.value += values[new_card.rank]
        if new_card.rank == "Ace":
            self.aces += 1
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
        return self.hand

#functions
def start_game():
    print("Welcome to BlackJack!")
    player_one = input("What is your name? ")
    cap = False
    while not cap:
        capital = input(f"Hi {player_one}, how much is your starting capital? ")
        try:
            capital = int(capital)
            if capital < 0 :
                print("Invalid input, please enter your starting capital")
                cap == False
            else:
                break
        except:
            print("Invalid input, please enter your starting capital")
            cap == False
    return player_one, capital

def create_player(player_one, cap):
    player1 = Player(player_one, cap)
    return player1

def place_bet():
    betting = True
    while betting:
        bet_amt = input("Please place your bet (in dollars): ")
        try:
            bet_amt = int(bet_amt)
            if bet_amt > 0 and bet_amt > player1.capital:
                print("Unable to place bet, Insufficient funds")
                print(f"Current capital: ${player1.capital}")
                betting == True
            elif bet_amt > 0 and bet_amt <= player1.capital:
                print(f"Bet amount of ${bet_amt} accepted")
                break
            else:
                print("Invalid bet amount!")
                betting == True
        except:
            print("Invalid bet amount, please enter a number")
            betting == True
    return bet_amt

def pdraw():
    while pdrawing == True:
        player_draw = input("\nPlayer, Hit or Stand? (h/s): ").lower()
        if player_draw not in ["h", "s"]:
            print("Invalid choice!")
            pdrawing == True
        elif player_draw == "h":
            player1.draw_one(new_deck.deal_one())
            print("\nPlayer hand:", player1)
            print("Player value: ", player1.value)
            if player1.value > 21:
                pdrawing == True
                return True
            else:
                pass
            pdrawing == True
        else:
            pdrawing == False
            return False

def ddraw(player1bust):
    while dealer.value <= 15:
        dealer.draw_one(new_deck.deal_one())

    if player1bust == True:
        if dealer.value > 15 and dealer.value <= 21:
            print("\n**DEALER WIN! Player Bust!**")
            print("\nDealer hand:", dealer)
            print("Dealer value:", dealer.value)
            return False
    else:
        pass
    
    if dealer.value < 17:
        while dealer.value < 17:
            dealer.draw_one(new_deck.deal_one())
    else:
        pass

    if dealer.value <= 21:
        return False
    else:
        return True

def check_double_aces(playervalue, dealervalue):
    if player1.value == dealer.value and player1.value == 22:
        print("\nBoth Player and Dealer Double Aces! Draw")
        print("\nPlayer hand:", player1)
        print("\nDealer hand:", dealer)
        return False
    elif player1.value == 22:
        player1.win_bet(bet_amt*3)
        print("\nPlayer Double Aces!")
        print("\nPlayer hand:", player1)
        print("\nDealer hand:", dealer)
        return False
    elif dealer.value == 22:
        player1.lose_bet(bet_amt*3)
        print("\nDealer Double Aces!")
        print("\nPlayer hand:", player1)
        print("\nDealer hand:", dealer)
        return False
    else:
        print("\nNo Double Aces")
        return True

def check_blackjack(playervalue, dealervalue, check):
    if blackjack_check == True:
        if player1.value == dealer.value and player1.value == 21:
            print("\n**Both player and dealer Blackjack! Draw**")
            print("\nPlayer hand:", player1)
            print("\nDealer hand:", dealer)
            return False
        elif player1.value == 21:
            player1.win_bet(bet_amt*2)
            print("\n**Player Blackjack!**")
            print("\nPlayer hand:", player1)
            print("\nDealer hand:", dealer)
            return False
        elif dealer.value == 21:
            player1.lose_bet(bet_amt*2)
            print("\n**Dealer Blackjack!**")
            print("\nPlayer hand:", player1)
            print("\nDealer hand:", dealer)
            return False
        else:
            print("\nNo Blackjack!")
            return True
    else:
        return False

def check_win(player1bust, dealerbust):
    if player1bust == True and dealerbust == True:
            print("\n**DRAW! Player and Dealer Bust**")
            print("\nDealer hand:", dealer)
            print("Dealer value:", dealer.value)
    elif player1bust == True and dealerbust == False:
        player1.lose_bet(bet_amt)
    elif player1bust == False and dealerbust == True:
        player1.win_bet(bet_amt)
        print("\n**PLAYER WIN! Dealer Bust!**")
        print("\nDealer hand:", dealer)
        print("Dealer value:", dealer.value)
    else:
        if player1.value > dealer.value:
            player1.win_bet(bet_amt)
            print("\n**PLAYER WIN!**")
            print("\nDealer hand:", dealer)
            print("Dealer value:", dealer.value)
        elif player1.value < dealer.value:
            player1.lose_bet(bet_amt)
            print("\n**DEALER WIN!**")
            print("\nDealer hand:", dealer)
            print("Dealer value:", dealer.value)
        else:
            print("\n**DRAW!**")
            print("\nDealer hand:", dealer)
            print("Dealer value:", dealer.value)

def cont_game():
    if player1.capital <= 0:
        print("\nGame Over! No funds available")
        return False
    else:
        choice = ""
        while choice not in ["Y", "N"]:
            choice = input("\nOne more round? (Y or N): ").upper()
            if choice not in ["Y", "N"]:
                print("Sorry, I dont' understand, please choose Y or N")
        if choice == "Y":
            return True
        else:
            print("\nGame Over!")
            return False

#game set up
player_one, capital = start_game()
player1 = create_player(player_one, capital)
print(f"\nStarting capital: ${player1.capital} ")

game_on = True

while game_on:
    #placing bet
    bet_amt = place_bet()

    #dealing cards
    dealer = Dealer()
    player1 = create_player(player1.name, player1.capital)
    new_deck = Deck()
    new_deck.shuffle()

    for i in range(2):
        player1.draw_one(new_deck.deal_one())
        dealer.draw_one(new_deck.deal_one())

    print("\nPlayer hand:", player1)
    print("Player value: ", player1.value)
    print("\nDealer hand:\n**Hidden**")
    print(dealer.hand[1])

    #drawing phase
    blackjack_check =  False
    blackjack_check = check_double_aces(player1.value, dealer.value)
    pdrawing = check_blackjack(player1.value, dealer.value, blackjack_check)
    if pdrawing == True:
        player1bust = False
        player1bust = pdraw()
        dealerbust = False
        dealerbust = ddraw(player1bust)
        check_win(player1bust, dealerbust)
    print(f"\nCurrent capital: ${player1.capital} ")
    game_on = cont_game()