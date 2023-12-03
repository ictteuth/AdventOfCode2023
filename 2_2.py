#!/usr/bin/env python 
'''Advent of Code 2023 - Day 2 - Part 2

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

What is the fewest number of cubes of each color that could have been in the bag to make the game possible?

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
'''

from icecream import ic

infile = "c:/Users/Ian/Documents/AdventOfCode2023/2in.txt"

input = open(infile, 'r')

def isPossible(game, rgb):
    return game['red'] <= rgb[0] and game['green'] <= rgb[1] and game['blue'] <= rgb[2]


if __name__ == "__main__":
    games = ['Game 0 placeholder']
    for line in input:
        
        game_score = {'red' : 0, 'green' : 0, 'blue' : 0}

        line = line.strip()
        game = line.split(':')

        #ignore everything before the :
        #
        pulls = game[1].split(';')
        for pull in pulls:
            colors = pull.split(',')
            for color in colors:
                color = color.strip().split(' ')
                #keep track of the largest pull for each color
                game_score[color[1]] = max(game_score[color[1]], int(color[0]))
        games.append(game_score)

    #check which games are possible
    #add those game numbers together
    sum = 0
    for n in range(1,len(games)):
        sum += games[n]['red'] * games[n]['green'] * games[n]['blue'] 
    ic(sum)



