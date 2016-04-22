def int_to_time(seconds):
    time=Time()
    minutes,time.second=divmod(seconds,60)
    time.hour,time.minute=divmod(minutes,60)
    return time

class Time(object):

    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __str__(self):
        return "%.2d:%.2d:%.2d" %(self.hour,self.minute,self.second)

    def __add__(self, other):
        if isinstance(other,Time):
            seconds=self.time_to_int()+other.time_to_int()
            return int_to_time(seconds)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __cmp__(self, other):
        return self.second-other.second

    def print_time(self):
        print "%.2d:%.2d:%.2d" %(self.hour,self.minute,self.second)

    def time_to_int(self):
        minutes=self.hour*60+self.minute
        seconds=minutes*60+self.second
        return seconds

    def increment(self,seconds):
        seconds+=self.time_to_int()
        return int_to_time(seconds)

    def is_after(self,other):
        return self.time_to_int()>other.time_to_int()




class Card(object):
    """
    Represents a standard playing card.
    """
    suit_names=["Clubs", "Demonds","Hearts","Spades"]
    rank_names=[None,"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

    def __init__(self,suit=0,rank=2):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return "%s of %s" %(Card.rank_names[self.rank],Card.suit_names[self.suit])

    def __cmp__(self, other):
        # check the suit
        if self.suit>other.suit:
            return 1
        if self.suit<other.suit:
            return -1

        #check the rank
        if self.rank>other.rank:
            return 1
        if self.rank<other.rank:
            return -1

        return 0
import random
class Deck(object):
    """

    """

    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(1,14):
                card=Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self,card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self,num_of_hand,nums_of_card):
        res=[]
        for i in range(num_of_hand):
            hand=Hand(label="%d") %(i)
            for j in nums_of_card[i]:
                hand.add_card(self.pop_card())
            res.append(hand)
        return res

class  Hand(Deck):
    """
    Represents a hand of playing cards.
    """
    def __init__(self,label=""):
        self.cards=[]
        self.label=label

if __name__=="__main__":
    hand=Hand("new hand")
    deck=Deck()
    card=deck.pop_card()
    hand.add_card(card)
    print hand
