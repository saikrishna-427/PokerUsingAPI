''' 1)  I am going to take deck of cards using API
    2)  pick the hand of cards using deck-id'''

import requests
import json


class Cards_API:
    #test class

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '{} of {}'.format(self.rank,self.suit)


class Deck_API:
    '''Used this class to create deck of cards ++ reshuffle the deck of cards using
    deck-id of new deck ++ and also used a function to draw a card through API'''
    def __init__(self):
        self.f = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        # deck_of_cards = self.f.json()
        self.deck_id = self.f.json()['deck_id']

    def __str__(self):
        return self.deck_id

    def reshuffle(self):
        self.shuffle = requests.post('https://deckofcardsapi.com/api/deck/'+self.deck_id+'/shuffle/')
        return None

    def draw_a_card(self,num_of_cards):
        '''Draw a card from deck'''
        self.cards_in_hand = dict()
        self.num_of_cards = num_of_cards
        self.draw = requests.get('https://deckofcardsapi.com/api/deck/'+self.deck_id+
                            '/draw/?count='+str(self.num_of_cards))
        for i in range(self.num_of_cards):
            self.drew_card_code = self.draw.json()['cards'][i]['code']
            self.drew_card_value = self.draw.json()['cards'][i]['value']
            self.drew_card_suit = self.draw.json()['cards'][i]['suit']
            self.cards_in_hand[self.drew_card_code]= [self.drew_card_value,self.drew_card_suit]
        # print(self.drew_card_code, self.drew_card_suit, self.drew_card_value)
        return self.cards_in_hand



class Hand_API(Deck_API):
    '''Using this class to return a list for cards taken by an instance'''

    def __init__(self):
        self.player_cards = []

    def draw(self,deck,num):
        for key,values in deck.draw_a_card(num).items():
            self.player_cards.append(values)
        return self.player_cards


    def __str__(self):
        return 'player cards are: {}'.format(self.player_cards)






# card = Cards_API('Hearts','10')
# print(card)

deck_api = Deck_API()

# deck_api.reshuffle()
# print(deck_api.draw_a_card(3))
# print(deck_api)
# print(deck_api.reshuffle())
# Player22 = Hand_API()
# print(Player22.draw(deck_api,7))


