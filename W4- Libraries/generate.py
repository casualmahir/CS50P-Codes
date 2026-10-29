#Picking a random item with random.choice
import random

coin = random.choice(["heads", "tails"])
print(coin)

#Picking a random integer with random.randint
import random

number = random.randint(1, 10)
print(number)

#Shuffling a list with random.shuffle
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
