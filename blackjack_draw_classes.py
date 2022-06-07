import numpy as np
import matplotlib.pyplot as plt
import random
from collections import defaultdict


# Initialize the deck and card values/types
card_types = ("ace", "two", "three", "four", "five", "six", "seven", 
              "eight", "nine", "ten", "jack", "queen", "king")

# TODO: implement deck as a class with the cards left/each card's count,
# and total cards in the deck
# TODO: also methods like bool hand_in_deck(deck, hand)
deck = {}
for i in card_types:
    deck[i] = 4

card_values = {}
for i in range(1, 11):
    card_values[card_types[i-1]] = i
card_values["jack"] = 10
card_values["queen"] = 10
card_values["king"] = 10


# Class for the deck of cards to draw from
class Deck():
    def __init__(self):
        self.card_types = ("ace", "two", "three", "four", "five", 
                        "six", "seven", "eight", "nine", "ten", 
                        "jack", "queen", "king")
        self.deck = {}
        for i in self.card_types:
            self.deck[i] = 4
        
        self.card_values = {}
        for i in range(1, 11):
            self.card_values[card_types[i-1]] = i
        self.card_values["jack"] = 10
        self.card_values["queen"] = 10
        self.card_values["king"] = 10

        self.total_cards = 52

        return

    # returns whether there is a specific card value
    # still in the deck
    def card_in_deck(self, card):
        return self.deck[card] != 0

    # resets the count for all cards in deck
    # NOTE: DOES NOTHING FOR HANDS THAT HAVE ALREADY
    # DRAWN CARDS
    def reset_deck(self):
        for i in self.deck:
            self.deck[i] = 4
        self.total_cards = 52
        return



# TODO: implement an averagerator class for stats purposes

# Class for various hand values and their possible hands
class StartValueHands():
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
    # TODO: use numpy for stats computing
    def graph_hands(self):
        n = 50000
        drawn_hands = {}
        for i in self.hands:
            drawn_hands[i] = 0
        for i in range(n):
            hand = self.choose_hand()
            drawn_hands[hand] += 1
        
        drawn_hands_normalized = {}
        for i in drawn_hands:
            drawn_hands_normalized[i] = drawn_hands[i] / n

        names = list(drawn_hands_normalized.keys())
        values = list(drawn_hands_normalized.values())

        plt.figure(figsize=[10,5])
        plt.xticks(fontsize=8)
        plt.bar(range(len(drawn_hands_normalized)), values, align='center')
        plt.xticks(range(len(drawn_hands_normalized)), names)
        plt.title(f"Hand Value = {self.hand_value}")
        plt.suptitle(f"n = {n}")
        plt.savefig('blackjack/graphs/hand_' + str(self.hand_value) + '.png', bbox_inches='tight')
        # plt.show()
        return

### HAND VALUE INITIALIZATION ###

# for each hand value tested, list possible hands

# hand value = 2 
two = StartValueHands(2)
two.hands =   [("ace", "ace")]
two.init_prob()

# hand value = 3 
three = StartValueHands(3)
three.hands =   [("ace", "two")]
three.init_prob()

# hand value = 4 
four = StartValueHands(4)
four.hands =   [("ace", "three"),
                ("two", "two")]
four.init_prob()

# hand value = 5 
five = StartValueHands(5)
five.hands =   [("ace", "four"),
                ("two", "three")]
five.init_prob()

# hand value = 6 
six = StartValueHands(6)
six.hands =   [("ace", "five"),
                ("two", "four"),
                ("three", "three")]
six.init_prob()

# hand value = 7 
seven = StartValueHands(7)
seven.hands =   [("ace", "six"),
                ("two", "five"),
                ("three", "four")]
seven.init_prob()

# hand value = 8 
eight = StartValueHands(8)
eight.hands =   [("ace", "seven"),
                ("two", "six"),
                ("three", "five"),
                ("four", "four")]
eight.init_prob()

# hand value = 9 
nine = StartValueHands(9)
nine.hands =    [("ace", "eight"),
                ("two", "seven"),
                ("three", "six"),
                ("four", "five")]
nine.init_prob()

# hand value = 10
ten = StartValueHands(10)
ten.hands =     [("ace", "nine"),
                ("two", "eight"),
                ("three", "seven"),
                ("four", "six"),
                ("five", "five")]
ten.init_prob()

# hand value = 11
eleven = StartValueHands(11)
eleven.hands = [("two", "nine"),
                ("three", "eight"),
                ("four", "seven"),
                ("five", "six"),]
eleven.init_prob()

# hand value = 12
twelve = StartValueHands(12)
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
thirteen = StartValueHands(13)
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
fourteen = StartValueHands(14)
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
fifteen = StartValueHands(15)
fifteen.hands = [("five", "ten"),
                ("five", "jack"),
                ("five", "queen"),
                ("five", "king"),
                ("six", "nine"),
                ("seven", "eight"),
                ("ace", "four")]
fifteen.init_prob()

# hand value = 16
sixteen = StartValueHands(16)
sixteen.hands = [("six", "ten"),
                ("six", "jack"),
                ("six", "queen"),
                ("six", "king"),
                ("seven", "nine"),
                ("eight", "eight"),
                ("ace", "five")]
sixteen.init_prob()

# hand value = 17
seventeen = StartValueHands(17)
seventeen.hands = [("seven", "ten"),
                ("seven", "jack"),
                ("seven", "queen"),
                ("seven", "king"),
                ("eight", "nine"),
                ("ace", "six")]
seventeen.init_prob()

# hand value = 18
eighteen = StartValueHands(18)
eighteen.hands = [("eight", "ten"),
                ("eight", "jack"),
                ("eight", "queen"),
                ("eight", "king"),
                ("nine", "nine"),
                ("ace", "seven")]
eighteen.init_prob()

# hand value = 19
nineteen = StartValueHands(19)
nineteen.hands = [("nine", "ten"),
                ("nine", "jack"),
                ("nine", "queen"),
                ("nine", "king"),
                ("ace", "eight")]
nineteen.init_prob()

# hand value = 20
twenty = StartValueHands(20)
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
twentyone = StartValueHands(21)
twentyone.hands = [("ten", "ace"),
                ("jack", "ace"),
                ("queen", "ace"),
                ("king", "ace"),]
twentyone.init_prob()


### END HAND VALUE INITIALIZATION ###

# define a dict mapping hand value objects to an integer
hand_values_dict = {2: two,
                    3: three,
                    4: four,
                    5: five,
                    6: six,
                    7: seven,
                    8: eight,
                    9: nine,
                    10: ten,
                    11: eleven,
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
        # idea: implement a deck class w/ deck dict and sum of cards
        i = random.randint(0, 52)
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
    # takes a dict of StartValueHands objects with integer keys
    # NOTE: assumes that deck is full before drawing starting hands
    def draw_starting_hand(self, start_value):
        start_hand = hand_values_dict[start_value].choose_hand()

        for i in start_hand:
            self.draw_specific(i)
        self.value = start_value
        return

    # reset the hand to an empty state
    # NOTE: Does not reset the deck the hand drew from
    def reset_hand(self):
        self.hand = ()
        self.value = 0
        return


# TODO: implement function to reset all hands and deck
# maybe put all hands in a list and iterate over list to reset them
# this will require reset methods for both hand and deck
def reset_hand_and_deck(hand):
    hand.reset_hand()
    for i in card_types:
        deck[i] = 4


# Test drawing a starting hand
test_hand = Hand()
test_hand.draw_starting_hand(17)
print(test_hand.hand)
print(test_hand.value)
print(deck)

# Graph the probability distributions for each starting value
#for i in range(11, 21):
    #hand_values_dict[i].graph_hands()

reset_hand_and_deck(test_hand)
print(test_hand.hand)
print(test_hand.value)
print(deck)

test_hand.draw_starting_hand(19)
print(test_hand.hand)
print(test_hand.value)
print(deck)

# Test graphing for 15
prob_test_hand = Hand()
reset_hand_and_deck(prob_test_hand)
trials = 50000
total_of_all_hands = 0
total_of_valid_hands = 0
num_valid_hands = 0
total_for_all_hands = defaultdict(lambda:0)
for n in range(trials):
    # print(n)
    prob_test_hand.draw_starting_hand(15)
    prob_test_hand.draw_random()
    # print(prob_test_hand.value)

    total_of_all_hands += prob_test_hand.value
    if prob_test_hand.value <= 21:
        num_valid_hands += 1
        total_of_valid_hands += prob_test_hand.value
        total_for_all_hands[prob_test_hand.value] += 1
    else:
        total_for_all_hands['Bust'] += 1
    
    reset_hand_and_deck(prob_test_hand)

print(total_for_all_hands)
print(num_valid_hands)



# TODO AND DATA TO GATHER:
# -----------------------
# probability of each hand value + bust after hitting
#   AKA probability of getting each possible hand value after hitting

# Output the numerical probability of busting
# after hitting and the average hand value of 
# the hand after hitting