import numpy as np
import re


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    total_points = 0
    # for each line read in winning numbers and played numbers, of the form
    # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    for line in lines:
        # get the winning numbers
        winning_numbers = line.split('|')[0].split(':')[1].split()
        # get the played numbers
        played_numbers = line.split('|')[1].split()


        # count the points
        points = 0.5
        for number in played_numbers:
            if number in winning_numbers:
                points *= 2
        #rounding down 0.5 to 0
        total_points += int(points)

    print(f'The total points are {total_points}')

    return


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    total_points = 0
    # for each line read in winning numbers and played numbers, of the form
    # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    card_matches = []
    for line in lines:
        # get the winning numbers
        winning_numbers = line.split('|')[0].split(':')[1].split()
        # get the played numbers
        played_numbers = line.split('|')[1].split()
        # count how many matches there are
        matches = 0
        for number in played_numbers:
            if number in winning_numbers:
                matches += 1
        card_matches.append(matches)
    card_wins = np.ones(card_matches.__len__())
    # for each card, count how many cards you actually win
    for i in range(card_matches.__len__(), 0, -1):
        for j in range(card_matches[i-1]):
            card_wins[i-1] += card_wins[i+j]

    #sum all the wins
    total_wins = np.sum(card_wins)
    print(f'The total wins are {total_wins}')
    return


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
