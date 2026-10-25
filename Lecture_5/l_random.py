import random

#coin = random.choice(["heads", "tails"]) #choice is a probabiltiy

#number = random.randint(1, 10) #choses a random number from 1 to 10

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)