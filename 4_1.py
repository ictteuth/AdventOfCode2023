#!/usr/bin/env python 
'''Advent of Code 2023 - Day 4 - Part 1

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

Card #: List of winning numbers | List of your numbers
Card point value = 2^(n-1) where n is the number of winning numbers you have
(0 points for n=0)

How many points are the cards worth in total?

'''

from icecream import ic

class Card:
    def __init__(self, cardStr):
        #discard the first part of the string
        self.winners = []
        self.numbers = []
        self.points = 0

        cardStr = cardStr.split(':')[1].strip()

        for numstr in cardStr.split('|')[0].strip().split(' '):
            if numstr:
                self.winners.append(int(numstr))

        for numstr in cardStr.split('|')[1].strip().split(' '):
            if numstr:
                self.numbers.append(int(numstr))
        
        matches = 0
        for x in self.numbers:
            if x in self.winners:
                matches += 1
        
        if matches > 0:
            self.points = 2**(matches-1)

infile = "c:/Users/Ian/Documents/AdventOfCode2023/4in.txt"

if __name__ == "__main__":
    with open(infile, 'r') as input:
        cardList = []
        sum = 0
        for line in input:
            card = Card(line.strip())
            cardList.append(card)
            sum += card.points
        ic(sum)
