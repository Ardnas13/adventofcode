from os import environ

def execute(input):
    x = 1
    xhistory = []
    cycle = 0
    for instruction in input:
        instruction = instruction.strip()
        if instruction == 'noop':
            cycle += 1
            xhistory.append(x)
        else:
            cycle += 1
            xhistory.append(x)
            addx = instruction.split(' ')[1]
            sub, addx = (True, int(addx[1:])) if addx[0] == '-' else (False, int(addx))
            cycle += 1
            xhistory.append(x)
            x = x - addx if sub else x + addx
    xhistory.append(x)
    return xhistory

def signal_strength(xhistory):
    result = 0
    for i in range(19,220,40):
        result += xhistory[i] * (i+1)
    return result

def getSolutionPart1():
    return signal_strength(execute(open("input.txt", "r")))

def draw(cycle, sprite):
    return  '#' if (cycle - 1) % 40 in sprite else '.'

def pixel_execute(input):
    x = 1
    sprite = [0,1,2]
    cycle = 0
    result = ''
    for instruction in input:
        instruction = instruction.strip()
        if instruction == 'noop':
            cycle += 1
            result += draw(cycle, sprite)
        else:
            cycle += 1
            result += draw(cycle, sprite)
            addx = instruction.split(' ')[1]
            sub, addx = (True, int(addx[1:])) if addx[0] == '-' else (False, int(addx))
            cycle += 1
            result += draw(cycle, sprite)
            x = x - addx if sub else x + addx
            sprite = [x-1,x,x+1]
    result += draw(cycle, sprite)
    return result

def getSolutionPart2():
    result = pixel_execute(open("input.txt", "r"))
    for i in range(0,239,40):
        print(result[i:i+40])

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2())
else:
    print(getSolutionPart1())