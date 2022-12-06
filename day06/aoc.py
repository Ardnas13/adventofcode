from os import environ
import re
import collections

def solution(i):
    input = open("input.txt", "r").readline()
    four_unique = []
    result = 0
    for char in input:
        if len(four_unique) == i:
            return result
        else:
            if char in four_unique:
                while four_unique[0] != char in four_unique:
                    four_unique.pop(0)
                four_unique.pop(0)
            four_unique.append(char)
            result += 1
    return -1

def getSolutionPart1():
    return solution(4)

def getSolutionPart2():
    return solution(14)

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2())
else:
    print(getSolutionPart1())