infile = "c:/Users/Ian/Documents/AdventOfCode2023/1in1.txt"

input = open(infile, 'r')
'''
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
'''
text_digits = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "zero" : 0
}

def is_text_digit(line, n):
    try:
        s = line[n:n+3]
    except:
        return (False, -1)
    if s in text_digits:
        return (True, text_digits[s])
    try:
        s = line[n:n+4]
    except:
        return (False, -1)
    if s in text_digits:
        return (True, text_digits[s])
    try:
        s = line[n:n+5]
    except:
        return (False, -1)
    if s in text_digits:
        return (True, text_digits[s])
    return (False, 0)


fixed_sum = 0

for line in input:
    for n in range(len(line)):
        if line[n].isdigit():
            fixed_sum = fixed_sum + 10*int(line[n])
#            print('f#')
            break
        text_result = is_text_digit(line, n)
        if text_result[0]:
            fixed_sum = fixed_sum + 10*text_result[1]
#            print('fW')
            break

    for n in range(len(line)-1, -1, -1):
        if line[n].isdigit():
            fixed_sum = fixed_sum + int(line[n])
#            print('b#')
            break
        text_result = is_text_digit(line, n)
        if text_result[0]:
            fixed_sum = fixed_sum + text_result[1]
#            print('bW')
            break

print(fixed_sum)

