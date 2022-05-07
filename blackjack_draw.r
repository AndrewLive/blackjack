# simulate the initial deck of 52
card_values <- c("ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king")
deck <- rep(card_values, 4)

# initialize the hand values we will test
tested_hand_values <- c(11:20)

# start with a hand of 2 cards from the deck
hand <- sample(card_values, size = 2, replace = FALSE)
cat("starting hand: ", hand, "\n")

# map the deck cards to their numerical values


# "hit" and gain one more card
hit_card <- sample(card_values, size = 1, replace = FALSE)
cat("hit card: ", hit_card, "\n")

hand <- append(hand, hit_card)
cat("new hand: ", hand, "\n")