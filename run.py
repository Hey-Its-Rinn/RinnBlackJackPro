from classes.BlackJack import BlackJack


print('\u2663')  # club
print('\u2660')  # spade
print('\u2665')  # heart
print('\u2666')  # diamond
print('')

# print('\u0332')
# print('aaa\u0332zzz') #underlines last a
# print('aaa'+'\u0332'+'zzz') #underlines last a
# print('113'+'\u0332'+'zzz') #underlines first z
# print('11a'+'\u0332'+'zzz') #underlines a
# print('\033[4mhello\033[0m')
# print(' '+'\u0332'+'1')


def clear_screen():
    print('\n' * 50)


def stop():
    a = input('ENTER to continue.')


# TODO: create main function
def main():
    game = BlackJack()
    game.new_game()

    while True:
        game.new_round()
        if game.bankrupt:
            clear_screen()
            print('\nWow! You are great at losing money!')
            print('\nYou leave with {} Monnies.'.format(str(game.money)))
            print('You can always get more Monnies to lose.\n')
            break

        if game.cash_out:
            clear_screen()
            print('\nI see you are tired of winning so much! Well, I hope that\'s why you\'re going anyway...')
            print('\nYou leave with {} Monnies.'.format(str(game.money)))
            print('Maybe you\'ll come back after your trip to the bank?\n')
            break

        game.display_cards()
        game.blackjack_check()
        if game.player_blackjack:
            if game.dealer_hand.cards[0][1]['value'] not in [10, 11]:
                game.pay_blackjack()
                continue
        game.double()
        if game.double_down:
            game.player_hand.cards += [game.get_card()]

        while True:
            game.display_cards()
            if game.stay:
                break
            if game.hit:
                game.player_hand.cards += [game.get_card()]
                game.hit = False
                if game.player_hand.check_score() > 21:
                    game.player_bust = True
                    game.stay = True
            game.player_decision()

        game.dealer_hand.cards[1][1]['hidden'] = False
        if game.dealer_hand.check_score() == 21:
            game.dealer_blackjack = True
        clear_screen()
        game.display_cards()
        print('The dealer has revealed their hole card.')
        print('They will hit if they have less than 17...\n')
        stop()
        while game.dealer_hand.check_score() < 17:
            game.dealer_hand.cards += [game.get_card()]
        if game.dealer_hand.check_score() > 21:
            game.dealer_bust = True
        clear_screen()
        game.display_cards()
        print('The round is over. \n')
        stop()
        game.win_check()
        game.sweep_cards()

# TODO: create main routine

while True:
    main()
    play_again = input('Restart game (yes/no): ')
    if play_again.lower() == 'yes' or play_again.lower() == 'y':
        continue
    if play_again.lower() == 'no' or play_again.lower() == 'n':
        break