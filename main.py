import random

def deal_p2(available):
    """deals cards to p2 from the 39 available cards after dealing to p1"""
    available_p2_cards = available[:]
    p2_cards = []
    # deal 13 cards to p2 (add those cards to p2_cards list)
    for x in range(13):
        random_card = random.choice(available_p2_cards)
        p2_cards.append(random_card)
        available_p2_cards.remove(random_card)
    return p2_cards

def check_high_cards(hand):
    """checks for any high cards in a hand and sums up the score and returns it"""
    total_score = 0
    for card in hand:
        if 'A' in card:
            total_score += 4
        elif 'K' in card:
            total_score += 3
        elif 'Q' in card:
            total_score += 2
        elif 'J' in card:
            total_score += 1

    return total_score

def check_doubleton(hand, suit):
    total = 0
    return total

def check_singleton(hand, suit):
    total = 0
    return total

def check_void(hand):
    total = 0
    return total

# standard 52 card deck
cards = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '0C', 'JC', 'QC', 'KC',
         'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '0D', 'JD', 'QD', 'KD',
         'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '0H', 'JH', 'QH', 'KH',
         'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '0S', 'JS', 'QS', 'KS']

# available_cards takes copy of cards to start off
available_cards = cards[:]
p1_cards = []
total_points = 0

# deal 13 cards to p1 (add those cards to p1_cards list)
for i in range(13):
    rand_card = random.choice(available_cards)
    p1_cards.append(rand_card)
    available_cards.remove(rand_card)

print("p1 cards: ", p1_cards)

# print("available_cards: ", available_cards)
# print("size of available cards: ", len(available_cards))

# simulation -> calculate score n times
for i in range(1):
    p2_cards = deal_p2(available_cards)
    print("p2 cards: ", p2_cards)

    total_points = check_high_cards(p1_cards) + check_high_cards(p2_cards)
    print("total points:", total_points)
