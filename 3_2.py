#!/usr/bin/env python 
'''Advent of Code 2023 - Day 3 - Part 2


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

A gear is any '*' symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.

Find the sum of all gear ratios
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

    def scanForNumbers(self, sch):
        r = 0
        c = 0

        for r in range(len(sch)):
            c = 0
            while c < len(sch[r]):
                if sch[r][c].isdigit():
                    length = self.scanNumber(sch, r, c)
                    c += length-1
                c += 1

    def scanForGears(self, sch):
        r = 0
        c = 0
        gearSum = 0
        for r in range(len(sch)):
            for c in range(len(sch[r])):
                if sch[r][c] == '*':
                    gearSum += self.scanGear(sch, r, c)
        return gearSum

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

    def scanGear(self, sch: list[list[str]], r: int, c: int) -> int:
        numberCount = 0
        gearRatio = 1
        for r2 in range(r-1, r+2):
            c2 = c-1
            while c2 < c+2:
                try:
                    if sch[r2][c2].isdigit():
                        (length_fw, value) = self.scanGearNumber(sch, r2, c2)
                        numberCount += 1
                        gearRatio *= value
                        c2 += length_fw
                except:
                    pass
                c2 += 1

        #after checking all around
        if not numberCount == 2:
            gearRatio = 0
        return gearRatio

    def scanGearNumber(self, sch: list[list[str]], r: int, c: int):
        origin = c
        start = c
        end = c
        #find the start of the number
        while start >= 1 and sch[r][start-1].isdigit():
            start -= 1
        
        #find the end of the number
        while end < len(sch[r])-1 and sch[r][end+1].isdigit():
            end += 1

        return (end-origin, int(sch[r][start:end+1]))

infile = "c:/Users/Ian/Documents/AdventOfCode2023/3in.txt"

if __name__ == "__main__":
    with open(infile, 'r') as input:
        schematic = [line.strip() for line in input]
        pnscanner = PNScanner()
        pnscanner.scanForNumbers(schematic)

        sum = 0
        for number in pnscanner.PNList:
            if number.symbolAdjacent:
                sum += number.value
        ic(sum)

        gearSum = pnscanner.scanForGears(schematic)
        ic(gearSum)

