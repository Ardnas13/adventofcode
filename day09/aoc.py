from os import environ

def move(direction, knot):
    x,y = knot
    if direction == 'R':
        x += 1
    elif direction == 'L':
        x -= 1
    elif direction == 'U':
        y += 1
    elif direction == 'D':
        y -= 1
    return (x,y)

def follow(tail, head):
    hx, hy = head
    tx, ty = tail
    if hy == ty:
        if hx-tx > 1:
            return move('R',(tx,ty))
        elif hx-tx < -1:
            return move('L',(tx,ty))
    elif hx == tx:
        if hy-ty > 1:
            return move('U',(tx,ty))
        elif hy-ty < -1:
            return move('D',(tx,ty))
    elif hx - tx < -1 and hy - ty > 0 or hx - tx < 0 and hy - ty > 1:
        return (tx-1,ty+1)
    elif hx - tx > 1 and hy - ty > 0 or hx - tx > 0 and hy - ty > 1:
        return (tx+1,ty+1)
    elif hx - tx > 1 and hy - ty < 0 or hx - tx > 0 and hy - ty < -1:
        return (tx+1,ty-1)
    elif hx - tx < -1 and hy - ty < 0 or hx - tx < 0 and hy - ty < -1:
        return (tx-1,ty-1)
    return (tx,ty)

def getSolutionPart1():
    input = open('input.txt', 'r')
    h = (0,0)
    t = (0,0)
    positions_visited = set()
    for instruction in input:
        instruction = instruction.split()
        direction, nbr_steps = instruction[0], int(instruction[1])
        for i in range(nbr_steps):
            h = move(direction, h)
            t = follow(t, h)
            positions_visited.add(t)
    return len(positions_visited)

def getSolutionPart2():
    input = open('input.txt', 'r')
    knots = [(0,0) for i in range(10)]
    positions_visited = set()
    for instruction in input:
        instruction = instruction.split()
        direction, nbr_steps = instruction[0], int(instruction[1])
        for i in range(nbr_steps):
            for i in range(10):
                if i == 0:
                    knots[i] = move(direction, knots[i])
                else:   
                    knots[i] = follow(knots[i], knots[i-1])
                if i == 9:
                    positions_visited.add(knots[i])
    return len(positions_visited)

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2())
else:
    print(getSolutionPart1())