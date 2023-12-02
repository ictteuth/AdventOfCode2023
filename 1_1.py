infile = "c:/Users/Ian/Documents/AdventOfCode2023/1in1.txt"

input = open(infile, 'r')

sum = 0

for line in input:
    for character in line:
#        print(character)
        if character.isdigit():
            sum = sum + 10*int(character)
            break

    for character in reversed(line):
        if character.isdigit():
            sum = sum + int(character)
            break

print(sum)