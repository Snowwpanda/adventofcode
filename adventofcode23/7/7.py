import numpy as np
import re
import time
from collections import Counter


def sorted_string(cards1):
    # Convert the string to a list
    string_list = list(cards1)

    # Sort the list
    string_list.sort()

    # Convert the list back to a string
    sorted_string = ''.join(string_list)

    return sorted_string

class class_hand:
    cards = ''
    value = 0

    def __init__(self, cards, value):
        self.cards = cards
        self.value = value

    def __lt__(self, other):
        lessthan_bool =  self.compare_hand(self.cards, other.cards) == -1
        return lessthan_bool

    def __eq__(self, other):
        return self.compare_hand(self.cards, other.cards) == 0

    def compare_high_card(self, cards1, cards2):
        value_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
        for i in range(5):
            if value_map[cards1[i]] > value_map[cards2[i]]:
                return 1
            if value_map[cards1[i]] < value_map[cards2[i]]:
                return -1
        return 0


    def compare_hand(self, cards1, cards2):
        if cards1 == cards2:
            return 0
        sign = 1
        if self.compare_high_card(cards1, cards2) == 1:
            sorted_1 = sorted_string(cards1)
            sorted_2 = sorted_string(cards2)
        else:
            sorted_1 = sorted_string(cards2)
            sorted_2 = sorted_string(cards1)
            sign = -1

        # check for five of a kind
        if re.search(r'([1-9AKQJT])\1{4}', sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])\1{4}', sorted_2):
            return -sign
        # check for four of a kind
        if re.search(r'([1-9AKQJT])(\1){3}', sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])(\1){3}', sorted_2):
            return -sign
        # check for full house
        if re.search(r'([1-9AKQJT])(\1){2}([1-9AKQJT])(\3)', sorted_1) or re.search(r'([1-9AKQJT])(\1)([1-9AKQJT])(\3){2}',
                                                                                   sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])(\1){2}([1-9AKQJT])(\3)', sorted_2) or re.search(r'([1-9AKQJT])(\1)([1-9AKQJT])(\3){2}',
                                                                                   sorted_2):
            return -sign
        # check for three of a kind
        if re.search(r'([1-9AKQJT])(\1){2}', sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])(\1){2}', sorted_2):
            return -sign
        # check for two pairs
        if re.search(r'([1-9AKQJT])(\1).?([1-9AKQJT])(\3)', sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])(\1).?([1-9AKQJT])(\3)', sorted_2):
            return -sign
        # check for one pair
        if re.search(r'([1-9AKQJT])(\1)', sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])(\1)', sorted_2):
            return -sign
        return sign






class class_hand_jokers:
    cards = ''
    value = 0

    def most_common_card(self, cards1):
        if re.match(r'^J+$', cards1):
            return 'J'
        counter = Counter(cards1.replace('J', ''))
        most_common = counter.most_common(1)[0][0]
        return most_common


    def __init__(self, cards, value):
        self.cards = cards
        self.value = value

    def __lt__(self, other):
        lessthan_bool =  self.compare_hand(self.cards, other.cards) == -1
        return lessthan_bool

    def __eq__(self, other):
        return self.compare_hand(self.cards, other.cards) == 0

    def compare_high_card(self, cards1, cards2):
        value_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
        for i in range(5):
            if value_map[cards1[i]] > value_map[cards2[i]]:
                return 1
            if value_map[cards1[i]] < value_map[cards2[i]]:
                return -1
        return 0


    def compare_hand(self, cards1, cards2):
        if cards1 == cards2:
            return 0
        # get the most common card from a hand that is not a J


        sign = 1
        if self.compare_high_card(cards1, cards2) == 1:
            sorted_1 = sorted_string(cards1.replace('J', self.most_common_card(cards1)))
            sorted_2 = sorted_string(cards2.replace('J', self.most_common_card(cards2)))
        else:
            sorted_1 = sorted_string(cards2.replace('J', self.most_common_card(cards2)))
            sorted_2 = sorted_string(cards1.replace('J', self.most_common_card(cards1)))
            sign = -1

        # check for five of a kind
        if re.search(r'([1-9AKQJT])\1{4}', sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])\1{4}', sorted_2):
            return -sign
        # check for four of a kind
        if re.search(r'([1-9AKQJT])(\1){3}', sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])(\1){3}', sorted_2):
            return -sign
        # check for full house
        if re.search(r'([1-9AKQJT])(\1){2}([1-9AKQJT])(\3)', sorted_1) or re.search(r'([1-9AKQJT])(\1)([1-9AKQJT])(\3){2}',
                                                                                   sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])(\1){2}([1-9AKQJT])(\3)', sorted_2) or re.search(r'([1-9AKQJT])(\1)([1-9AKQJT])(\3){2}',
                                                                                   sorted_2):
            return -sign
        # check for three of a kind
        if re.search(r'([1-9AKQJT])(\1){2}', sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])(\1){2}', sorted_2):
            return -sign
        # check for two pairs
        if re.search(r'([1-9AKQJT])(\1).?([1-9AKQJT])(\3)', sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])(\1).?([1-9AKQJT])(\3)', sorted_2):
            return -sign
        # check for one pair
        if re.search(r'([1-9AKQJT])(\1)', sorted_1):
            return sign
        if re.search(r'([1-9AKQJT])(\1)', sorted_2):
            return -sign
        return sign






def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # read in hands, hands are of the form [1-9AKQJT]{5}\s*\d+\s*
    hands = []
    for line in lines:
        if re.search('[1-9AKQJT]{5}\s*\d+\s*', line):
            hands.append( class_hand(line.split()[0], int(line.split()[1])) )

    # sort hands by first value with costum sort function compare_hand
    hands.sort()

    winnings = 0
    rank = 1
    for hand in hands:
        print(f"{hand.cards} {hand.value} {rank}")
        winnings += hand.value * rank
        rank += 1

    print(f'The total winnings are {winnings}')
    return


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # read in hands, hands are of the form [1-9AKQJT]{5}\s*\d+\s*
    hands = []
    for line in lines:
        if re.search('[1-9AKQJT]{5}\s*\d+\s*', line):
            hands.append( class_hand_jokers(line.split()[0], int(line.split()[1])) )

    # sort hands by first value with costum sort function compare_hand
    hands.sort()

    winnings = 0
    rank = 1
    for hand in hands:
        print(f"{hand.cards} {hand.value} {rank}")
        winnings += hand.value * rank
        rank += 1

    print(f'The total winnings are {winnings}')
    return



if __name__ == '__main__':
    solveA('input.txt')

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
