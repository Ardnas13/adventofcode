from os import environ
import re
import collections

def createList(start, stop):
    return list(range(start, stop + 1))

def moveCrates1(crates, moves):
    crates_copy = crates.copy()
    for move in moves:
        for i in range(move[0]):
            crate= crates_copy[move[1] - 1].pop(0)
            crates_copy[move[2] - 1].insert(0, crate)
    return crates_copy

def moveCrates2(crates, moves):
    crates_copy = crates.copy()
    for move in moves:
        crate = crates_copy[move[1] - 1][:move[0]]
        del crates_copy[move[1] - 1][:move[0]]
        crates_copy[move[2] - 1] = crate + crates_copy[move[2] - 1]
    return crates_copy

def solution(whichone):
    resulting_crates = ""
    crates = {}
    isMoves = False
    moves = []
    input = open("input.txt", "r")
    while input:
        line = input.readline()
        if line == '':
            break
        if isMoves:
            move = [int(x) for x in line.replace('\n','').split(' ') if  x.isnumeric()]
            moves.append(move)
        if line == '\n':
            isMoves = True     
        else:
            for i, letter in enumerate(line[1::4]):
                if letter.isupper():
                    if i in crates:
                        crates[i] += [letter]
                    else:
                        crates[i] = [letter]
    if whichone:
        res_crates = moveCrates1(crates, moves)
    else:
        res_crates = moveCrates2(crates, moves)
    for i in range(len(res_crates)):
        resulting_crates += res_crates[i].pop(0)
    return resulting_crates

def getSolutionPart1():
    return solution(True)

def getSolutionPart2():
    return solution(False)

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2())
else:
    print(getSolutionPart1())