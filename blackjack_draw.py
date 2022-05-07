import random

# simulate the initial deck and card values
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


# deal a hand of 2 cards
hand = ()
for i in range(2):
    card = (card_types[random.randint(0, 12)], )
    deck[card[0]] -= 1
    hand += card

print("current hand:", hand)

# hit to recieve a new card
hit = (card_types[random.randint(0, 12)], )
deck[hit[0]] -= 1

print("hit card:", hit)

hand += hit
print("new hand:", hand)

