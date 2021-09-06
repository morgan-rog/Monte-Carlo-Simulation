import random

cards = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '0C', 'JC', 'QC', 'KC',
         'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '0D', 'JD', 'QD', 'KD',
         'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '0H', 'JH', 'QH', 'KH',
         'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '0S', 'JS', 'QS', 'KS']

# available_cards takes copy of cards to start off
available_cards = cards[:]
p1_cards = []

# deal 13 cards to p1 (add those cards to p1_cards list)
for i in range(13):
    rand_card = random.choice(available_cards)
    p1_cards.append(rand_card)
    available_cards.remove(rand_card)

print(p1_cards)
print(available_cards)
print("size: ", len(available_cards))