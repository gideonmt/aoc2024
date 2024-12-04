testMode = False

example_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

data = example_input if testMode else open(__file__.replace('.py', '.in')).read()

lines = data.strip().split('\n')

p1 = 0
p2 = 0

for report in lines:
    lvls = list(map(int, report.split()))
    diffs = [lvls[i+1] - lvls[i] for i in range(len(lvls) - 1)]
    inc = all(1 <= d <= 3 for d in diffs)
    dec = all(-3 <= d <= -1 for d in diffs)
    if inc or dec:
        p1 += 1
        p2 += 1
    else:
        for i in range(len(lvls)):
            dlvls = lvls[:i] + lvls[i+1:]
            ddiffs = [dlvls[j+1] - dlvls[j] for j in range(len(dlvls) - 1)]
            dinc = all(1 <= d <= 3 for d in ddiffs)
            ddec = all(-3 <= d <= -1 for d in ddiffs)
            if dinc or ddec:
                p2 += 1
                break

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
