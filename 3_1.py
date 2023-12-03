#!/usr/bin/env python 
'''Advent of Code 2023 - Day 3 - Part 1


467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

Find sum of all numbers adjacent to a symbol

'''

from icecream import ic

class PartNumber:
    def __init__(self, sRow, sCol, value, symbolAdjacent):
        self.sRow = sRow
        self.sCol = sCol
        self.value = value
        self.symbolAdjacent = symbolAdjacent

class PNScanner:
    def __init__(self):
        self.PNList = []

    def scanSchematic(self, sch):
        r = 0
        c = 0

        for r in range(len(sch)):
            c = 0
            while c < len(sch[r]):
                if sch[r][c].isdigit():
                    length = self.scanNumber(sch, r, c)
                    c += length-1
                c += 1

    def scanNumber(self, sch: list[list[str]], r: int, c: int):
        length = 1
        symbolFound = False
        
        #start with the first digit
        value = int(sch[r][c])

        #find the whole number
        while c+length <= len(sch[r])-1 and sch[r][c+length].isdigit():
            value *= 10
            value += int(sch[r][c+length])
            length += 1

        #Scan all around
        #....????....
        #....?##?....
        #....????....
        for r2 in range(r-1, r+2):
            for c2 in range(c-1, c+length+1):
                if symbolFound:
                    break
                try:
                    if not sch[r2][c2].isdigit() and not sch[r2][c2] == '.':
                        #found symbol adjacent
                        symbolFound = True
                except:
                    #out of schematic range
                    continue


        number = PartNumber(r, c, value, symbolFound)
        self.PNList.append(number)
        return length

infile = "c:/Users/Ian/Documents/AdventOfCode2023/3in.txt"

if __name__ == "__main__":
    with open(infile, 'r') as input:
        schematic = [line.strip() for line in input]
        pnscanner = PNScanner()
        pnscanner.scanSchematic(schematic)

        sum = 0
        for number in pnscanner.PNList:
            if number.symbolAdjacent:
                sum += number.value
        ic(sum)

    
    #walk through the schematic finding numbers and checking around them for symbols
    

