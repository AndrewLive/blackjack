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
    card_values[card_types[i]] = i
card_values["jack"] = 10
card_values["queen"] = 10
card_values["king"] = 10


# Class for the player's hand and its value
class Hand():
    def __init__(self):
        self.hand = ()
        self.value = 0
        return
    
    # draw one card from the deck
    # does not add the value of the card to the hand
    def __draw__(self):
        i = random.randint(0, 12)
        while(deck[card_types[i]] == 0):
            i = random.randint(0, 12)
        
        self.hand += (card_types[i], )
        deck[card_types[i]] -= 1
        return
    
    # draw the cards for the desired starting hand value
    # takes a dict of HandValueHands objects with integer keys
    def draw_starting_hand(self, start_value):
        pass


# class for various hand values and their possible hands
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
eleven.graph_hands()

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
twelve.graph_hands()

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
thirteen.graph_hands()

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
fourteen.graph_hands()

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
fifteen.graph_hands()

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
sixteen.graph_hands()

# hand value = 17
seventeen = HandValueHands(17)
seventeen.hands = [("seven", "ten"),
                ("seven", "jack"),
                ("seven", "queen"),
                ("seven", "king"),
                ("eight", "nine"),
                ("ace", "six")]
seventeen.init_prob()
seventeen.graph_hands()

# hand value = 18
eighteen = HandValueHands(18)
eighteen.hands = [("eight", "ten"),
                ("eight", "jack"),
                ("eight", "queen"),
                ("eight", "king"),
                ("nine", "nine"),
                ("ace", "seven")]
eighteen.init_prob()
eighteen.graph_hands()

# hand value = 19
nineteen = HandValueHands(19)
nineteen.hands = [("nine", "ten"),
                ("nine", "jack"),
                ("nine", "queen"),
                ("nine", "king"),
                ("ace", "eight")]
nineteen.init_prob()
nineteen.graph_hands()

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
twenty.graph_hands()

