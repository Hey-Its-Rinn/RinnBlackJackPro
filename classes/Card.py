class Card:
    '''
    This is a card.
    Just feed it a list with list[0] as card_name and list[1] as a dict with the cards info.

    IMAGE_VALUE_CODES stores the inoformation on how to build a card.
    0 indicates a blank space.
    1 indeicates a suit character.
    Other characters are as-is for their repective value.
    '''
    IMAGE_VALUE_CODES = {'2': '01000000010',
                         '3': '01000100010',
                         '4': '10100000101',
                         '5': '10100100101',
                         '6': '10101010101',
                         '7': '10111010101',
                         '8': '10111011101',
                         '9': '11101110111',
                         '10': '11111011111',
                         'J': 'JAK11111JAK',
                         'Q': 'QUE11111QUE',
                         'K': 'KIN11111KIN',
                         'A': 'ACE00100ACE'}

    SUIT_CODES = {'hearts': '\u2665',
                  'diamonds': '\u2666',
                  'clubs': '\u2663',
                  'spades': '\u2660'}

    def __init__(self, card):
        self.card = card
        self.name = card[0]
        self.type = str(card[1]['type'])
        self.value = card[1]['value']
        self.suit = card[1]['suit']
        self.hidden = card[1]['hidden']

    def image(self):
        '''
        Returns image of card as a list of each line.
        '''
        suit_code = self.SUIT_CODES[self.suit]

        # Decoded Card Values(dcv)

        if not self.hidden:
            dcv = self.IMAGE_VALUE_CODES[self.type].replace('0', ' ').replace('1', suit_code)
            if self.type == '10':
                top_corner = str(self.type)
                bottom_corner = str(self.type)
            else:
                top_corner = str(self.type) + ' '
                bottom_corner = ' ' + str(self.type)
        else:
            dcv = '           '
            top_corner = '? '
            bottom_corner = ' ?'

        image = ['\u256d' + '\u2500' * 11 + '\u256e',
                 '\u2502 ' + top_corner + '        \u2502',
                 '\u2502   {} {} {}   \u2502'.format(dcv[0], dcv[1], dcv[2]),
                 '\u2502     {}     \u2502'.format(dcv[3]),
                 '\u2502   {} {} {}   \u2502'.format(dcv[4], dcv[5], dcv[6]),
                 '\u2502     {}     \u2502'.format(dcv[7]),
                 '\u2502   {} {} {}   \u2502'.format(dcv[8], dcv[9], dcv[10]),
                 '\u2502        ' + bottom_corner + ' \u2502',
                 '\u2570' + '\u2500' * 11 + '\u256f']
        return image
