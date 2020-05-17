import unittest

from classes.BlackJack import BlackJack

class TestBlackJack(unittest.TestCase):

    def setUp(self):
        # instantiate class
        self.game = BlackJack()

    def test___init__(self):
        '''
        test___init__ method
        '''

        # asserts
        self.assertEqual(self.game.money, 0)
        self.assertEqual(self.game.shoe, {})

    def test_new_game_money_is_correct(self):
        # instantiate new_game
        self.game.new_game()

        # asserts
        self.assertEqual(self.game.money, 10000)

    def test_new_game_copy_all_dicts_from_DECK_to_shoe(self):
        # instantiate new_game
        self.game.new_game()

        # asserts
        self.assertEqual(self.game.shoe, self.game.DECK)

if __name__ == '__main__':
    unittest.main()
