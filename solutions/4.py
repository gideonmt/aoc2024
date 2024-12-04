testMode = False

example_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

data = example_input if testMode else open(__file__.replace('.py', '.in')).read()

lines = data.strip().split('\n')

word = 'XMAS'
p1 = 0
for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]:
            found = True
            for k in range(len(word)):
                ni, nj = i + k * dx, j + k * dy
                if ni < 0 or ni >= len(lines) or nj < 0 or nj >= len(line) or lines[ni][nj] != word[k]:
                    found = False
                    break
            if found:
                p1 += 1

print(p1)

p2 = 0

grid = [list(line) for line in lines]

for i in range(1, len(grid) - 1): 
    for j in range(1, len(grid[i]) - 1):
        tl = grid[i - 1][j - 1]
        br = grid[i + 1][j + 1]
        tr = grid[i - 1][j + 1]
        bl = grid[i + 1][j - 1]
        c = grid[i][j]
        diag1_valid = tl + c + br in ("MAS", "SAM")
        diag2_valid = tr + c + bl in ("MAS", "SAM")
        if diag1_valid and diag2_valid:
            p2 += 1

print(p2)
