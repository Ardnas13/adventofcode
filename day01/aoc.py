from os import environ


def getSolutionPart1():
    most_calories = 0
    temp = []
    file1 = open("input.txt", "r")
    while file1:
        line  = file1.readline()
        if line == '\n':
            total_calories = sum(temp)
            if total_calories > most_calories:
                most_calories = total_calories
            temp.clear()
        elif line == "":
            break
        else:
            temp.append(int(line))
    return most_calories

def argmax(listlike):
    return max(range(len(listlike)), key=lambda x : listlike[x])

def getSolutionPart2():
    total_top_three_calories = 0
    elves_calories = []
    temp = []
    file1 = open("input.txt", "r")
    while file1:
        line  = file1.readline()
        if line == '\n':
            elves_calories.append(sum(temp))
            temp.clear()
        elif line == "":
            break
        else:
            temp.append(int(line)) 
    for i in range(3):
        total_top_three_calories += max(elves_calories)
        del elves_calories[argmax(elves_calories)]
    return total_top_three_calories

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2())
else:
    print(getSolutionPart1())