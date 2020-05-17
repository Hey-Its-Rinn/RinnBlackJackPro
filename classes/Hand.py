class Hand:
    """
    is a list of cards and the score
    """

    def __init__(self):
        self.cards = []
        self.size = len(self.cards)

    def check_score(self):
        score = 0
        aces = 0
        for card in self.cards:
            if card[1]['type'] == 'A':
                aces += 1
        for card in self.cards:
            score += card[1]['value']
        while (score > 21) and (aces >= 1):
            score -= 10
            aces -= 1
        return score
