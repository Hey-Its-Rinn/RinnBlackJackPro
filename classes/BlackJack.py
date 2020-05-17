import random

from classes.Hand import Hand
from classes.Card import Card


def clear_screen():
    print('\n' * 50)


def stop():
    a = input('ENTER to continue.')


class BlackJack:
    """
    base class for BlackJack game
    """

    # TODO - create deck dict
    DECK = ({
        'ace_of_hearts': {'type': 'A', 'value': 11, 'suit': 'hearts'},
        'two_of_hearts': {'type': 2, 'value': 2, 'suit': 'hearts'},
        'three_of_hearts': {'type': 3, 'value': 3, 'suit': 'hearts'},
        'four_of_hearts': {'type': 4, 'value': 4, 'suit': 'hearts'},
        'five_of_hearts': {'type': 5, 'value': 5, 'suit': 'hearts'},
        'six_of_hearts': {'type': 6, 'value': 6, 'suit': 'hearts'},
        'seven_of_hearts': {'type': 7, 'value': 7, 'suit': 'hearts'},
        'eight_of_hearts': {'type': 8, 'value': 8, 'suit': 'hearts'},
        'nine_of_hearts': {'type': 9, 'value': 9, 'suit': 'hearts'},
        'ten_of_hearts': {'type': 10, 'value': 10, 'suit': 'hearts'},
        'jack_of_hearts': {'type': 'J', 'value': 10, 'suit': 'hearts'},
        'queen_of_hearts': {'type': 'Q', 'value': 10, 'suit': 'hearts'},
        'king_of_hearts': {'type': 'K', 'value': 10, 'suit': 'hearts'},
        'ace_of_diamonds': {'type': 'A', 'value': 11, 'suit': 'diamonds'},
        'two_of_diamonds': {'type': 2, 'value': 2, 'suit': 'diamonds'},
        'three_of_diamonds': {'type': 3, 'value': 3, 'suit': 'diamonds'},
        'four_of_diamonds': {'type': 4, 'value': 4, 'suit': 'diamonds'},
        'five_of_diamonds': {'type': 5, 'value': 5, 'suit': 'diamonds'},
        'six_of_diamonds': {'type': 6, 'value': 6, 'suit': 'diamonds'},
        'seven_of_diamonds': {'type': 7, 'value': 7, 'suit': 'diamonds'},
        'eight_of_diamonds': {'type': 8, 'value': 8, 'suit': 'diamonds'},
        'nine_of_diamonds': {'type': 9, 'value': 9, 'suit': 'diamonds'},
        'ten_of_diamonds': {'type': 10, 'value': 10, 'suit': 'diamonds'},
        'jack_of_diamonds': {'type': 'J', 'value': 10, 'suit': 'diamonds'},
        'queen_of_diamonds': {'type': 'Q', 'value': 10, 'suit': 'diamonds'},
        'king_of_diamonds': {'type': 'K', 'value': 10, 'suit': 'diamonds'},
        'ace_of_clubs': {'type': 'A', 'value': 11, 'suit': 'clubs'},
        'two_of_clubs': {'type': 2, 'value': 2, 'suit': 'clubs'},
        'three_of_clubs': {'type': 3, 'value': 3, 'suit': 'clubs'},
        'four_of_clubs': {'type': 4, 'value': 4, 'suit': 'clubs'},
        'five_of_clubs': {'type': 5, 'value': 5, 'suit': 'clubs'},
        'six_of_clubs': {'type': 6, 'value': 6, 'suit': 'clubs'},
        'seven_of_clubs': {'type': 7, 'value': 7, 'suit': 'clubs'},
        'eight_of_clubs': {'type': 8, 'value': 8, 'suit': 'clubs'},
        'nine_of_clubs': {'type': 9, 'value': 9, 'suit': 'clubs'},
        'ten_of_clubs': {'type': 10, 'value': 10, 'suit': 'clubs'},
        'jack_of_clubs': {'type': 'J', 'value': 10, 'suit': 'clubs'},
        'queen_of_clubs': {'type': 'Q', 'value': 10, 'suit': 'clubs'},
        'king_of_clubs': {'type': 'K', 'value': 10, 'suit': 'clubs'},
        'ace_of_spades': {'type': 'A', 'value': 11, 'suit': 'spades'},
        'two_of_spades': {'type': 2, 'value': 2, 'suit': 'spades'},
        'three_of_spades': {'type': 3, 'value': 3, 'suit': 'spades'},
        'four_of_spades': {'type': 4, 'value': 4, 'suit': 'spades'},
        'five_of_spades': {'type': 5, 'value': 5, 'suit': 'spades'},
        'six_of_spades': {'type': 6, 'value': 6, 'suit': 'spades'},
        'seven_of_spades': {'type': 7, 'value': 7, 'suit': 'spades'},
        'eight_of_spades': {'type': 8, 'value': 8, 'suit': 'spades'},
        'nine_of_spades': {'type': 9, 'value': 9, 'suit': 'spades'},
        'ten_of_spades': {'type': 10, 'value': 10, 'suit': 'spades'},
        'jack_of_spades': {'type': 'J', 'value': 10, 'suit': 'spades'},
        'queen_of_spades': {'type': 'Q', 'value': 10, 'suit': 'spades'},
        'king_of_spades': {'type': 'K', 'value': 10, 'suit': 'spades'}
    })

    # TODO: create init method
    def __init__(self):
        self.money = 0
        self.shoe = {}
        self.recycle = {}
        self.bet_amount = 0
        self.minimum_bet = 100
        self.bet_increment = 100
        self.double_down = False
        self.stay = False
        self.hit = False
        self.blackjack_winnings_multiplier = 1.5
        self.normal_winnings_multiplier = 1
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.dealer_blackjack = False
        self.player_blackjack = False
        self.dealer_bust = False
        self.player_bust = False
        self.push = False
        self.win = False
        self.lose = False
        self.bankrupt = False
        self.cash_out = False

    # TODO: create new game method
    def new_game(self):
        self.money = 10000
        for _ in self.DECK:
            self.shoe[_] = self.DECK[_]
        self.recycle = {}

    # TODO: create a round method
    def new_round(self):

        self.bet_amount = self.bet()
        self.money = self.money - self.bet_amount
        self.double_down = False
        self.stay = False
        self.hit = False
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.dealer_blackjack = False
        self.player_blackjack = False
        self.dealer_bust = False
        self.player_bust = False
        self.push = False
        self.win = False
        self.lose = False
        if self.bankrupt or self.cash_out:
            return
        self.deal()

    def bet(self):
        clear_screen()
        errors = []
        bet_instructions = ['You have this many Monnies: ' + str(self.money),
                            'The minimum bet is {} Monnies.'.format(str(self.minimum_bet)),
                            'Blackjack wins {} times your bet.'.format(str(self.blackjack_winnings_multiplier)),
                            'Otherwise, winnings are {} times your bet.'.format(str(self.normal_winnings_multiplier)),
                            'Your bet must be a whole number and a multiple of {}.\n'.format(str(self.bet_increment))]
        for line in bet_instructions: print(line)

        while True:

            if self.minimum_bet > self.money:
                clear_screen()
                self.bankrupt = True
                return 0

            clear_screen()
            for _ in errors:
                print(_)
            errors = []
            print('')
            for line in bet_instructions: print(line)
            proposed_bet = input('How much are you betting? You may also type "cash out" to leave: ')

            if proposed_bet.lower() == 'cash out':
                self.cash_out = True
                return 0

            if proposed_bet.isdigit():
                proposed_bet = int(proposed_bet)
                if proposed_bet % self.bet_increment != 0:
                    errors += ['\n     Your bet must be an multiple of {}!'.format(self.bet_increment)]

                if proposed_bet > self.money:
                    errors += ['\n     You can\'t bet more than you have!\n']

                if proposed_bet < self.minimum_bet:
                    errors += ['\n     You can\'t bet less than the minimum bet!\n']

            else:
                errors += ['\n     Invalid Input :( \n']

            if len(errors) > 0:
                continue
            else:
                return proposed_bet

    def deal(self):
        self.player_hand.cards = [self.get_card(), self.get_card()]
        self.dealer_hand.cards = [self.get_card(), self.get_card()]
        self.dealer_hand.cards[1][1]['hidden'] = True

    # TODO: create get_card method
    def get_card(self):
        if self.shoe == {}:
            for _ in self.recycle:
                self.shoe[_] = self.recycle[_]
            self.recycle = {}

        # gets a random card (a dict) from shoe and casts it to a list.
        random_card = random.choice(list(self.shoe.items()))
        random_card[1]['hidden'] = False

        # random_card[0] grabs the key for the card in the shoe.
        card = random_card[0]

        # random_card[1] grabs the nested dict for the card, which stores the card data.
        # card_type = self.random_card[1]['type']
        # card_value = self.random_card[1]['value']
        # card_suite = self.random_card[1]['suit']

        # removes the card from the shoe.
        del self.shoe[card]

        return random_card

    # TODO: create check score method
    def blackjack_check(self):

        # Player blackjack? This is instant win.
        if self.player_hand.check_score() == 21:
            self.player_blackjack = True

        # Dealer blackjack?
        if self.dealer_hand.check_score() == 21:
            self.dealer_blackjack = True

    def display_cards(self):
        all_player_hand_lines = []
        player_hand_line = ''
        all_dealer_hand_lines = []
        dealer_hand_line = ''
        lines = 9

        for index in range(0, lines):
            for card_info in self.dealer_hand.cards:
                card = Card(card_info)
                dealer_hand_line += card.image()[index]
            all_dealer_hand_lines.append(dealer_hand_line)
            dealer_hand_line = ''

        for index in range(0, lines):
            for card_info in self.player_hand.cards:
                card = Card(card_info)
                player_hand_line += card.image()[index]
            all_player_hand_lines.append(player_hand_line)
            player_hand_line = ''

        clear_screen()

        print('Dealer\'s cards: \n')

        for line in all_dealer_hand_lines:
            print(line)

        if self.dealer_bust:
            print('BUST')

        if not self.dealer_hand.cards[1][1]['hidden']:
            if self.dealer_blackjack:
                print('BLACKJACK')
        print('\n')
        print('Your cards: \n')

        for line in all_player_hand_lines:
            print(line)

        print('')

        if self.player_bust:
            print('BUST\n')

        if self.player_blackjack:
            print('BLACKJACK\n')

        if self.double_down:
            a = '(Doubled Down!)'
        else:
            a = ''

        if self.push:
            print('The round has resulted in a push...')
            print('You get to keep your bet of {}{}.\n'.format(self.bet_amount, a))
            return
        elif self.win:
            print('YOU BEAT THE DEALER!')
            print('Your bet of {}{} has been matched!\n'.format(self.bet_amount, a))
            return
        elif self.lose:
            print('YOU DID NOT BEAT THE DEALER!')
            print('The dealer will keep your bet of {}{}.\n'.format(self.bet_amount, a))
            return

        print('You bet {} Monnies{}.'.format(self.bet_amount, a))
        # print('You have {} Monnies left to play'.format(self.money))
        print('')

    def pay_blackjack(self):
        winnings = self.bet_amount * self.blackjack_winnings_multiplier
        print('You got a BlackJack and the dealer did not!')
        print('You won {}'.format(winnings))
        self.money += self.bet_amount + winnings
        print('You now have a balance of {} Monnies.'.format(self.money))
        stop()

    def player_decision(self):
        while True:
            if self.player_bust:
                break
            clear_screen()
            self.display_cards()
            print('You may Hit to receive another card, or Stay.\n')
            choice = input('Enter (h)it or (s)tay: ')
            if choice in ['h', 'hit']:
                self.hit = True
                break
            if choice in ['s', 'stay']:
                self.stay = True
                break

    def double(self):
        while True:
            print('You have the option to double your bet.')
            print('If you choose to double down, you will be dealt one additional card and must then stand.\n')
            player_decision = input('Would you like to double your bet? (y)es/(n)o: ')
            if player_decision.lower() in ['y', 'yes']:
                if self.money >= self.bet_amount:
                    self.money -= self.bet_amount
                    self.bet_amount += self.bet_amount
                    self.double_down = True
                    self.stay = True
                    self.display_cards()
                    break

                else:
                    print('\nYou can\'t double down because you don\'t have enough Monnies!')
                    stop()
                    break
            if player_decision.lower() in ['n', 'no']:
                break
            else:
                self.display_cards()
                continue

    def win_check(self):
        if (self.player_hand.check_score() == self.dealer_hand.check_score()) and \
                (self.player_hand.check_score() <= 21):
            self.push = True
            self.display_cards()
            stop()
            self.money += self.bet_amount
            return

        if ((self.player_hand.check_score() > self.dealer_hand.check_score()) and not self.player_bust) or \
                (self.dealer_bust and not self.player_bust):
            self.win = True
            self.display_cards()
            stop()
            self.money += self.bet_amount * 2
            return

        self.lose = True
        self.display_cards()
        stop()
        self.bet_amount = 0

    def sweep_cards(self):
        for _ in self.player_hand.cards:
            self.recycle[_[0]] = _[1]
        for _ in self.dealer_hand.cards:
            self.recycle[_[0]] = _[1]
