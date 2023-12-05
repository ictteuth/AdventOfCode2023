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
        self.winners = []
        self.numbers = []
        self.matches = 0
        self.cardNumber = int(cardStr.split(':')[0].strip().split(' ')[-1])

        cardStr = cardStr.split(':')[1].strip()

        for numstr in cardStr.split('|')[0].strip().split(' '):
            if numstr:
                self.winners.append(int(numstr))

        for numstr in cardStr.split('|')[1].strip().split(' '):
            if numstr:
                self.numbers.append(int(numstr))
        
        for x in self.numbers:
            if x in self.winners:
                self.matches += 1
    
class Deck:
    def __init__(self, infile):
        self.cards = []
        self.multipliers = {}
        self.lastCard = 0

        with open(infile, 'r') as input:
            for line in input:
                card = Card(line.strip())
                self.cards.append(card)
                self.lastCard = card.cardNumber
                self.multipliers[card.cardNumber] = 1

        for card in self.cards:
            for n in range(card.cardNumber + 1, card.cardNumber + 1 + card.matches):
                if n <= self.lastCard:
                    self.multipliers[n] += self.multipliers[card.cardNumber]
        

    def countCards(self):
        total = 0
        for id in self.multipliers:
            total += self.multipliers[id]
        return total
        

infile = "c:/Users/Ian/Documents/AdventOfCode2023/4in.txt"

if __name__ == "__main__":
    deck = Deck(infile)
    total = deck.countCards()
    ic(total)