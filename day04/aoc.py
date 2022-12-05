from os import environ
import re

def createList(start, stop):
    return list(range(start, stop + 1))

def checkOverlap(allOrAny):
    result = 0
    input = open("input.txt", "r")
    while input:
        line = input.readline()
        if line != '':
            line  = re.split('-|,', line)
            numbers = [int(x.strip()) for x in line]
            first = createList(numbers[0],numbers[1])
            second = createList(numbers[2],numbers[3])
            if allOrAny == 'all':
                if (all(x in first for x in second)) or (all(x in second for x in first)):
                    result += 1
            elif allOrAny == 'any':
                if (any(x in first for x in second)) or (any(x in second for x in first)):
                    result += 1
        else:
            break
    return result

def getSolutionPart1():
    return checkOverlap('all')

def getSolutionPart2():
    return checkOverlap('any')

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2())
else:
    print(getSolutionPart1())