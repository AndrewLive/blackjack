import numpy as np
import matplotlib.pyplot as plt
import random


# Initialize the deck and card values/types
card_types = ("ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king")
deck = {}
for i in card_types:
    deck[i] = 4

card_values = {}
for i in range(1, 11):
    card_values[card_types[i-1]] = i
card_values["jack"] = 10
card_values["queen"] = 10
card_values["king"] = 10


# Class for various hand values and their possible hands
class HandValueHands():
    def __init__(self, hand_value):
        self.hands = []
        self.hand_prob = {}
        self.total_hands = 0
        self.hand_value = hand_value
    
    # Function to calculate the number of total hands
    # and set the probabilities for each
    # CALL THIS AFTER DEFINING THE POSSIBLE HANDS
    def init_prob(self):
        for i in self.hands:
            if i[0] == i[1]:
                # 6 possible suite combinations for 2 same cards
                self.hand_prob[i] = 6
                self.total_hands += 6
                continue
            # 16 possible suite combinations for 2 different cards
            self.hand_prob[i] = 16
            self.total_hands += 16
    
    # choose a random hand from the possible hands of
    # the hand value according to probabilities
    def choose_hand(self):
        i = random.randint(0, self.total_hands - 1)
 
        for k in self.hands:
            i -= self.hand_prob[k]
            if i < 0:
                return k
    
    # graph the probability distribution of each possible hand
    def graph_hands(self):
        drawn_hands = {}
        for i in self.hands:
            drawn_hands[i] = 0
        for i in range(50000):
            hand = self.choose_hand()
            drawn_hands[hand] += 1

        names = list(drawn_hands.keys())
        values = list(drawn_hands.values())

        plt.figure(figsize=[10,5])
        plt.xticks(fontsize=8)
        plt.bar(range(len(drawn_hands)), values, align='center')
        plt.xticks(range(len(drawn_hands)), names)
        plt.title(f"Hand Value = {self.hand_value}")
        plt.show()
        return

### HAND VALUE INITIALIZATION ###

# for each hand value tested, list possible hands

# hand value = 11
eleven = HandValueHands(11)
eleven.hands = [("ace", "ten"),
                ("ace", "jack"),
                ("ace", "queen"),
                ("ace", "king"),
                ("two", "nine"),
                ("three", "eight"),
                ("four", "seven"),
                ("five", "six"),]
eleven.init_prob()

# hand value = 12
twelve = HandValueHands(12)
twelve.hands = [("ace", "ace"),
                ("two", "ten"),
                ("two", "jack"),
                ("two", "queen"),
                ("two", "king"),
                ("three", "nine"),
                ("four", "eight"),
                ("five", "seven"),
                ("six", "six"),]
twelve.init_prob()

# hand value = 13
thirteen = HandValueHands(13)
thirteen.hands = [("three", "ten"),
                ("three", "jack"),
                ("three", "queen"),
                ("three", "king"),
                ("four", "nine"),
                ("five", "eight"),
                ("six", "seven"),
                ("ace", "two")]
thirteen.init_prob()

# hand value = 14
fourteen = HandValueHands(14)
fourteen.hands = [("four", "ten"),
                ("four", "jack"),
                ("four", "queen"),
                ("four", "king"),
                ("five", "nine"),
                ("six", "eight"),
                ("seven", "seven"),
                ("ace", "three")]
fourteen.init_prob()

# hand value = 15
fifteen = HandValueHands(15)
fifteen.hands = [("five", "ten"),
                ("five", "jack"),
                ("five", "queen"),
                ("five", "king"),
                ("six", "nine"),
                ("seven", "eight"),
                ("ace", "four")]
fifteen.init_prob()

# hand value = 16
sixteen = HandValueHands(16)
sixteen.hands = [("six", "ten"),
                ("six", "jack"),
                ("six", "queen"),
                ("six", "king"),
                ("seven", "nine"),
                ("eight", "eight"),
                ("ace", "five")]
sixteen.init_prob()

# hand value = 17
seventeen = HandValueHands(17)
seventeen.hands = [("seven", "ten"),
                ("seven", "jack"),
                ("seven", "queen"),
                ("seven", "king"),
                ("eight", "nine"),
                ("ace", "six")]
seventeen.init_prob()

# hand value = 18
eighteen = HandValueHands(18)
eighteen.hands = [("eight", "ten"),
                ("eight", "jack"),
                ("eight", "queen"),
                ("eight", "king"),
                ("nine", "nine"),
                ("ace", "seven")]
eighteen.init_prob()

# hand value = 19
nineteen = HandValueHands(19)
nineteen.hands = [("nine", "ten"),
                ("nine", "jack"),
                ("nine", "queen"),
                ("nine", "king"),
                ("ace", "eight")]
nineteen.init_prob()

# hand value = 20
twenty = HandValueHands(20)
twenty.hands = [("ten", "ten"),
                ("ten", "jack"),
                ("ten", "queen"),
                ("ten", "king"),
                ("jack", "jack"),
                ("jack", "queen"),
                ("jack", "king"),
                ("queen", "queen"),
                ("queen", "king"),
                ("king", "king"),
                ("ace", "nine")]
twenty.init_prob()

# hand value = 21
twentyone = HandValueHands(21)
twentyone.hands = [("ten", "ace"),
                ("jack", "ace"),
                ("queen", "ace"),
                ("king", "ace"),]
twentyone.init_prob()


### END HAND VALUE INITIALIZATION ###

# define a dict mapping hand value objects to an integer
hand_values_dict = {11: eleven,
                    12: twelve,
                    13: thirteen,
                    14: fourteen,
                    15: fifteen,
                    16: sixteen,
                    17: seventeen,
                    18: eighteen,
                    19: nineteen,
                    20: twenty,
                    21: twentyone}


# Class for the player's hand and its value
class Hand():
    def __init__(self):
        self.hand = ()
        self.value = 0
        return
    
    # draw one random card from the deck
    def draw_random(self):
        #TODO CURRENTLY DOES NOT TAKE PROBABILITY
        #OF REMAINING CARDS INTO ACCOUNT
        #SHOULD BE OUT OF ALL REMAINING CARDS NOT
        #JUST CARD TYPES
        i = random.randint(0, 12)
        while(deck[card_types[i]] == 0):
            i = random.randint(0, 12)
        
        self.hand += (card_types[i], )
        deck[card_types[i]] -= 1
        # TODO TEST IF THE CARD VALUES MATH IS CORRECT
        self.value += card_values[card_types[i]]
        return

    # draw specified card
    # does nothing if the card isnt in deck
    def draw_specific(self, card):
        if deck[card] == 0:
            return

        self.hand += (card, )
        deck[card] -= 1
        # TODO TEST IF THE CARD VALUES MATH IS CORRECT
        self.value += card_values[card]
        return
    
    # draw the cards for the desired starting hand value
    # takes a dict of HandValueHands objects with integer keys
    # NOTE: assumes that deck is full before drawing starting hands
    def draw_starting_hand(self, start_value):
        start_hand = hand_values_dict[start_value].choose_hand()

        for i in start_hand:
            self.draw_specific(i)
        return


# Test drawing a starting hand
test_hand = Hand()
test_hand.draw_starting_hand(17)
print(test_hand.hand)
print(test_hand.value)
print(deck)

# Graph the probability distributions for each starting value
for i in hand_values_dict:
    hand_values_dict[i].graph_hands()