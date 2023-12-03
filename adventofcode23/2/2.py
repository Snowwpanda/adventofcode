import numpy as np
import re


def get_cubes_from_draw(draw):
    cubes = [0, 0, 0]
    for cube in draw.split(','):
        cube = cube.strip()
        if re.match('(\d+) red', cube):
            cubes[0] += int(re.match('(\d+) red', cube).group(1))
        elif re.match('(\d+) green', cube):
            cubes[1] += int(re.match('(\d+) green', cube).group(1))
        elif re.match('(\d+) blue', cube):
            cubes[2] += int(re.match('(\d+) blue', cube).group(1))
    return cubes


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # parse input, each line is of the form "Game 2: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    # we want a list starting with the game number, then a list of all drawn cubes, which are separated by a semicolon
    # the cubes can be red, green or blue, so we store them in a list of length 3

    # there can only be 12 red cubes, 13 green cubes, and 14 blue
    games_valid = {}
    sum_valid = 0
    games = []
    for line in lines:
        if not re.match('Game (\d+):.*', line):
            continue
        game = []
        game.append(int(re.match('Game (\d+):.*', line).group(1)))
        games_valid[game[0]] = True
        sum_valid += game[0]
        draws = re.match("Game (\d+): ?(.*)", line).group(2).split(';')
        for draw in draws:
            cubes = get_cubes_from_draw(draw)
            if cubes[0] > 12 or cubes[1] > 13 or cubes[2] > 14:
                if games_valid[game[0]]:
                    sum_valid -= game[0]
                games_valid[game[0]] = False
            game.append(cubes)
        games.append(game)

    print('The sum of invalid games is:')
    print(sum_valid)
    return


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # parse input, each line is of the form "Game 2: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    # we want a list starting with the game number, then a list of all drawn cubes, which are separated by a semicolon
    # the cubes can be red, green or blue, so we store them in a list of length 3

    # there can only be 12 red cubes, 13 green cubes, and 14 blue
    games_valid = {}
    sum_valid = 0
    games = []
    power = 0
    for line in lines:
        if not re.match('Game (\d+):.*', line):
            continue
        game = []
        game.append(int(re.match('Game (\d+):.*', line).group(1)))
        games_valid[game[0]] = True
        sum_valid += game[0]
        draws = re.match("Game (\d+): ?(.*)", line).group(2).split(';')
        max_cubes = [0, 0, 0]
        for draw in draws:
            cubes = get_cubes_from_draw(draw)
            max_cubes = np.maximum(max_cubes, cubes)
            game.append(cubes)
        games.append(game)
        power += max_cubes[0] * max_cubes[1] * max_cubes[2]

    print('The power is:')
    print(power)
    return


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
