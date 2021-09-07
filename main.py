import random


def print_hand(hand):
    """prints dealt hand in readable format"""
    for card in hand:
        print(card, end=" ")
    print()


def deal_p2(available):
    """deals cards to p2 from the 39 available cards after dealing to p1"""
    available_p2_cards = available[:]
    p2_cards_ = []
    # deal 13 cards to p2 (add those cards to p2_cards list)
    for x in range(13):
        random_card = random.choice(available_p2_cards)
        p2_cards_.append(random_card)
        available_p2_cards.remove(random_card)
    return p2_cards_


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
    """parameters are the hand and the suit character. Function returns either 0 or 1 score depending on if there are
    exactly 2 cards in that suit"""
    count = 0
    for card in hand:
        if suit in card:
            count += 1
    if count == 2:
        return 1
    else:
        return 0


def check_singleton(hand, suit):
    """parameters are the hand and the suit character. Function returns either 0 or 2 score depending on if there is
    exactly 1 card in that suit"""
    count = 0
    for card in hand:
        if suit in card:
            count += 1
    if count == 1:
        return 2
    else:
        return 0


def check_void(hand, suit):
    """parameters are the hand and the suit character. Function returns either 0 or 5 score depending on if there are
    zero cards in the suit"""
    count = 0
    for card in hand:
        if suit in card:
            count += 1
    if count == 0:
        return 5
    else:
        return 0


def get_best_outcome(score):
    if score < 20:
        return "Pass"
    elif score <= 25:
        return "Part score"
    elif score <= 31:
        return "Game"
    elif score <= 35:
        return "Small slam"
    else:
        return "Grand slam"


# standard 52 card deck
cards = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '0C', 'JC', 'QC', 'KC',
         'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '0D', 'JD', 'QD', 'KD',
         'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '0H', 'JH', 'QH', 'KH',
         'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '0S', 'JS', 'QS', 'KS']

# suits = Clubs, Diamonds, Hearts, Spades
suits = ['C', 'D', 'H', 'S']

choice = "y"

# number of simulated p2 hands
num_of_sims = 1000

while choice.lower() == "y":
    score_board = {
        "Pass": 0,
        "Part score": 0,
        "Game": 0,
        "Small slam": 0,
        "Grand slam": 0
    }

    # available_cards takes copy of cards to start off
    available_cards = cards[:]
    p1_cards = []

    # deal 13 cards to p1 (add those cards to p1_cards list)
    for i in range(13):
        rand_card = random.choice(available_cards)
        p1_cards.append(rand_card)
        available_cards.remove(rand_card)

    # calculate the score for p1's hand
    p1_hand_score = check_high_cards(p1_cards)
    for s in suits:
        p1_hand_score += check_doubleton(p1_cards, s) + check_singleton(p1_cards, s) + check_void(p1_cards, s)

    # print p1 hand info
    print("Here is your hand: ")
    print_hand(p1_cards)
    print("This hand is worth {} points.".format(p1_hand_score))
    print("Running simulation...\n")

    # simulation -> calculate score n times
    for i in range(num_of_sims):
        total_points = 0
        p2_cards = deal_p2(available_cards)

        # add p1 hand score and high card scores for p2 to total points
        total_points += p1_hand_score + check_high_cards(p2_cards)

        # add distribution scores for p2 to total points
        for s in suits:
            total_points += check_doubleton(p2_cards, s) + check_singleton(p2_cards, s) + check_void(p2_cards, s)

        outcome = get_best_outcome(total_points)
        score_board[outcome] += 1

    print("The estimated probability based on {} simulated hands: ".format(num_of_sims))
    for outcome in score_board:
        percentage = round(float(score_board[outcome] / num_of_sims) * 100, 2)
        print("{}: {}%".format(outcome, percentage))

    choice = input("\nAnother hand? (y/n) >> ")