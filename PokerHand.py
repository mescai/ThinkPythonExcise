"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *





class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        self.ranks={}
        for card in self.cards:
            self.ranks[card.rank]=self.ranks.get(card.rank,0)+1

    def has_pair(self):
        self.rank_hist()
        for rank in self.ranks.values():
            if rank==2:
                return True
        return False

    def has_two_pair(self):
        count=0
        self.rank_hist()
        for rank in self.ranks.values():
            if rank==2:
                count+=1
        if count==2:
            return True
        return False

    def has_three_kind(self):
         self.rank_hist()
         for rank in self.ranks.values():
             if rank==3:
                 return True
         return False

    def has_four_kind(self):
         self.rank_hist()
         for rank in self.ranks.values():
             if rank==4:
                 return True
         return False

    def has_straight(self):
        self.cards.sort(key=lambda x:x.rank)
        count=0
        previous=Card(suit=self.cards[0].suit,rank=self.cards[0].rank-1)
        for card in self.cards:
            if count==5:
                return True
            if count==4:
                if card.rank==previous.rank+1 or card.rank==previous.rank-12:
                    return True
                else:
                    count=1
                    previous=card
            if count<4:
                if card.rank==previous.rank+1:
                    count+=1
                    previous=card
                else:
                    count=1
                    previous=card
        return False

    def has_full_house(self):
        return self.has_pair() and self.has_three_kind()

    def has_straight_flush(self):
        self.cards.sort(key=lambda x:x.rank)
        count=0
        previous=Card(suit=self.cards[0].suit,rank=self.cards[0].rank-1)
        for card in self.cards:
            if count==5:
                return True
            if count==4:
                if card.rank==previous.rank+1 or card.rank==previous.rank-12:
                    if card.suit==previous.suit:
                        return True
                    else:
                        count=1
                        previous=card
                else:
                    count=1
                    previous=card
            if count<4:
                if card.rank==previous.rank+1 and card.suit==previous.suit:
                    count+=1
                    previous=card
                else:
                    count=1
                    previous=card
        return False




def classify(pohand):
    pohand.label="has none"
    if pohand.has_pair():
        pohand.label="pair"
    if pohand.has_two_pair():
        pohand.label="two pair"
    if pohand.has_three_kind():
        pohand.label="three of a kind"
    if pohand.has_straight():
        pohand.label="straight"
    if pohand.has_flush():
        pohand.label="flush"
    if pohand.has_full_house():
        pohand.label="full house"
    if pohand.has_four_kind():
        pohand.label="four of a kind"
    if pohand.has_straight_flush():
        pohand.label="straight flush"

def generate_hand(n):
    hist={}

    for i in range(n):
        deck=Deck()
        deck.shuffle()

        for j in range(7):
            hand=PokerHand()
            deck.move_cards(hand,7)

            classify(hand)
            hist[hand.label]=hist.setdefault(hand.label,0)+1
    return hist


if __name__ == '__main__':
    h=generate_hand(10000)


