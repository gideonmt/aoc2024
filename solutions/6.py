testMode = False

example_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

data = example_input if testMode else open(__file__.replace('.py', '.in')).read()

lines = data.strip().split('\n')

grid = [list(line) for line in lines]
rows, cols = len(grid), len(grid[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_map = {'^': 0, '>': 1, 'v': 2, '<': 3}

gp = None
dir = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] in dir_map:
            gp = (r, c)
            dir = dir_map[grid[r][c]]
            grid[r][c] = '.'
            break
    if gp:
        break

visited = set()
visited.add(gp)

while True:
    x, y = gp
    dx, dy = dirs[dir]
    nx, ny = x+dx,y+dy

    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '.':
        gp = (nx,ny)
        visited.add(gp)
    else:
        dir = (dir+1)%4

    nx,ny = gp[0]+dirs[dir][0],gp[1]+dirs[dir][1]
    if not (0 <= nx < rows and 0 <= ny < cols):
        break

p1 = len(visited)

p2 = 0
for i in range(rows):
    for j in range(cols):
        gp = None
        dir = None
        for r in range(rows):
            for c in range(cols):
                if lines[r][c] in dir_map:
                    gp = (r, c)
                    dir = dir_map[lines[r][c]]
                    break
            if gp:
                break

        visited = set()
        while True:
            x,y = gp
            dx,dy = dirs[dir]
            nx,ny = x+dx,y+dy

            if (gp,dir) in visited:
                p2 += 1
                break
            visited.add((gp,dir))

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '.' and (nx,ny) != (i,j):
                gp = (nx,ny)
            else:
                dir = (dir+1)%4

            nx,ny = gp[0]+dirs[dir][0],gp[1]+dirs[dir][1]
            if not (0 <= nx < rows and 0 <= ny < cols):
                break

print(p1)
print(p2)
