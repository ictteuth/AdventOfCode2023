#!/usr/bin/env python 
'''Advent of Code 2023 - Day 2 - Part 1'''

'''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

Which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
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
        if isPossible(games[n],[12,13,14]):
            sum += n
    ic(sum)



