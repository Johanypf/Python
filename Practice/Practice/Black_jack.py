hand_1 = ['J', 'A','A']
hand_2 = ['4', '7']

def hand_value(hand):
        value = 0
        values_A = 0 
        for card in hand:
            if card in ['J', 'Q', 'K']:
                value += 10
                
            elif card == 'A':
                value += 11
                values_A += 1

            else:
                value += int(card)

        while value > 21 and values_A > 0:
                value -= 10
                values_A -= 1

        return value



        
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False

    """

    if hand_value(hand_1) <= 21 and hand_value(hand_2) <= 21:
        return hand_value(hand_1) > hand_value(hand_2)
    elif hand_value(hand_1) > 21 and hand_value(hand_2) <= 21:
           return False
    elif hand_value(hand_1) <= 21 and hand_value(hand_2) > 21:
            return True
    else:
            return False
    
       

print(blackjack_hand_greater_than(hand_1, hand_2))