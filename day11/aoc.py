from os import environ
import math

def createNotes(input):
    notes = {}
    index = -1
    for row in input:
        if 'Monkey' in row:
            index += 1
            notes[index] = {}
        if 'items' in row:
            starting_worries = row.split(':')[1].strip().split(',')
            worries = []
            for worry in starting_worries:
                worries.append(int(worry.strip()))
            notes[index]['items'] = worries
        if 'Operation' in row:
            operation = row.split('old')[1].strip().split(' ')
            notes[index]['operation'] = operation
        if 'Test' in row:
            divisible = int(row.split('by')[1].strip())
            notes[index]['divisible'] = divisible
        if 'true' in row:
            iftrue = int(row.split('monkey')[1].strip())
            notes[index]['iftrue'] = iftrue
        if 'false' in row:
            iffalse = int(row.split('monkey')[1].strip())
            notes[index]['iffalse'] = iffalse
    return notes

def compute(old,operation):
    if operation[0] == '*':
        if len(operation) < 2:
            return old * old
        return old * int(operation[1])
    if operation[0] == '+':
        return old + int(operation[1])

def getSolutionPart1():
    notes = createNotes(open("input.txt", "r"))
    activity = [0] * len(notes.keys())
    for i in range(20):
        for key, note in notes.items():
            for item in note['items']:
                new_value = compute(item,note['operation'])
                new_value = new_value // 3
                if new_value % note['divisible'] == 0:
                    notes[note['iftrue']]['items'].append(new_value)
                else:
                    notes[note['iffalse']]['items'].append(new_value)
                activity[key] += 1
            note['items'].clear()
    activity.sort(reverse=True)
    return activity[0] * activity[1]

def getSolutionPart2():
    notes = createNotes(open("input.txt", "r"))
    activity = [0] * len(notes.keys())
    limit = math.lcm(2,3,5,7,11,13,17,19)
    for i in range(10000):
        for key, note in notes.items():
            for item in note['items']:
                new_value = compute(item,note['operation'])
                new_value = new_value % limit
                if new_value % note['divisible'] == 0:
                    notes[note['iftrue']]['items'].append(new_value)
                else:
                    notes[note['iffalse']]['items'].append(new_value)
                activity[key] += 1
            note['items'].clear()
    activity.sort(reverse=True)
    return activity[0] * activity[1]

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2())
else:
    print(getSolutionPart1())