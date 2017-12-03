input = "325489"

x = 50
y = 50

grid = [[0 for _ in xrange(100)] for _ in xrange(100)]

grid[y][x] = 1
x += 1


def sum_of_neighbours(x, y):
    s = 0
    for i in xrange(x-1, x+2):
        for j in xrange(y-1, y+2):
            if i == x and j == y:
                continue
            s += grid[j][i]
    return s


while True:
    z = sum_of_neighbours(x, y)
    grid[y][x] = z
    if grid[y][x-1] != 0 and grid[y-1][x] == 0:
        # go up
        y -= 1
    elif grid[y+1][x] != 0 and grid[y][x-1] == 0:
        # go left
        x -= 1
    elif grid[y][x+1] != 0 and grid[y+1][x] == 0:
        # go down
        y += 1
    elif grid[y-1][x] != 0 and grid[y][x+1] == 0:
        # go right
        x += 1

    if z > int(input):
        print z
        break
