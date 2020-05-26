
from PokerwithAPI_org import Deck_API,Hand_API

class PokerHand_API(Hand_API):

    def suit_hist(self):
        self.suits = {}
        for card in self.player_cards:
            suit = card[1]
            self.suits[suit] = self.suits.get(suit, 0) + 1
        return self.suits
            # self.suits[card[1]] = self.suits.get(card[1],0)+1

    def rank_hist(self):
        # pair: two cards with the same rank
        self.ranks = {}
        for card in self.player_cards:
            rank = card[1]
            self.ranks[rank] = self.ranks.get(rank, 0) + 1
        return self.ranks



    def has_a_flush(self):
        self.suit_hist()
        for val in self.suit_hist().values():
            if val >=5:
                return True
        return False

    def has_pair(self):
        self.rank_hist()
        for val in self.rank_hist().values():
            if val >=2:
                return True
            return False

    def has_two_pair(self):
        if self.has_pair() == False:
            return False
        else:
            count = 0
            for val in self.rank_hist().values():
                if val >= 2:
                    count += 1
            if count >= 2:
                return True
            else: return False

    def has_three_of_kind(self):
        self.rank_hist()
        for val in self.rank_hist().values():
            if val >= 3:
                return True
            return False

    def has_full_house(self):
        # full house: three cards with one rank, two cards with another
        self.rank_hist()
        three_of_kind = 0
        two_of_kind = 0
        for key,val in self.rank_hist().items():
            if val == 3:
                three_of_kind += 1
            if val == 2:
                two_of_kind +=1

        if three_of_kind == 1 and two_of_kind == 1:
            return True
        else:
            return False

    def has_four_of_kind(self):
        #four of a kind: four cards with the same rank
        self.rank_hist()
        for val in self.rank_hist().values():
            if val >= 4:
                return True
        return False


    def has_straight(self):
        '''straight: five cards with ranks in sequence
        (aces can be high or low, so Ace-2-3-4-5 is a straight
        and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)'''
        cards_in_suit = [None,"ACE", "2", "3", "4", "5", "6", "7",
                         "8", "9", "10", "JACK", "QUEEN", "KING", 'ACE']

        card1 = []

        for card in self.player_cards:
            card1.append(card[0])

        card2 = []
        for card in self.player_cards:
            # print(card[0])
            card2.append(card[0])
            if cards_in_suit.index(card[0]) > 10:
                pass
            else:
                for i in range(5):
                    if cards_in_suit[cards_in_suit.index(card[0]) + i] in card1:
                        card2.append(cards_in_suit[cards_in_suit.index(card[0]) + i])
                        card2 = list(dict.fromkeys(card2))
                        print(card2)
                    if len(card2) < 5:
                        card2 = []
                    else:
                        return True
        return False

    def classify:




deck_api = Deck_API()
# We already shuffuled cads before creating an instance
for i in range(5):
    hand = PokerHand_API()
    cards = hand.draw(deck_api,7) #1
    print(cards)
    print('Did player has a flush: '+str(hand.has_a_flush())) #2
    print('Did player has a pair: '+str(hand.has_pair())) #3
    print('Did player has two Pair: '+str(hand.has_two_pair()))
    print('Did player has three of kind: ' +str(hand.has_three_of_kind()))
    print('Did player has Full House: ' +str(hand.has_full_house()))
    print('Did player has four of kind: ' + str(hand.has_four_of_kind()))
    print('Did player has straight: ' + str(hand.has_straight()))




