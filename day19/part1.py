def peek(maze, x, y, direction):
    if direction == 'up':
        y -= 1
    if direction == 'down':
        y += 1
    if direction == 'left':
        x -= 1
    if direction == 'right':
        x += 1
    try:
        result = maze[y][x]
    except IndexError:
        result = " "
    return result


def part1(maze):
    direction = 'down'
    location = [0, maze[0].index('|')]
    seen = []

    while True:
        print location
        if direction == 'down':
            location[0] += 1
        elif direction == 'up':
            location[0] -= 1
        elif direction == 'left':
            location[1] -= 1
        elif direction == 'right':
            location[1] += 1

        try:
            tile = maze[location[0]][location[1]]
        except IndexError:
            tile = ' '
        print tile

        if tile == ' ':
            break
        elif tile not in {'|', '-', '+'}:
            seen.append(tile)
        elif tile == '+':
            # try original direction first
            if direction in ['down', 'up'] and peek(maze, location[1], location[0], direction) not in ['-', ' ']:
                continue
            elif direction in ['left', 'right'] and peek(maze, location[1], location[0], direction) not in ['|', ' ']:
                continue

            possibilities = ['left', 'right', 'up', 'down']
            if direction == 'down':
                possibilities.remove('up')
                possibilities.remove('down')
            elif direction == 'left':
                possibilities.remove('right')
                possibilities.remove('left')
            elif direction == 'right':
                possibilities.remove('left')
                possibilities.remove('right')
            elif direction == 'up':
                possibilities.remove('down')
                possibilities.remove('up')

            # try new directions
            direction = ""
            for p in possibilities:
                n = peek(maze, location[1], location[0], p)
                if p in ['left', 'right'] and n not in ['|', ' ']:
                    direction = p
                    break
                elif p in ['up', 'down'] and n not in  ['-', ' ']:
                    direction = p
                    break

            if not direction:
                break
    print "I guess it's game over?"
    return ''.join(seen)

lines = [l.strip('\n') for l in open('input.txt').readlines()]
print part1(lines)
