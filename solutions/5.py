testMode = False

example_input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

d = example_input if testMode else open(__file__.replace('.py', '.in')).read()

s1, s2 = d.strip().split('\n\n')

r = [tuple(map(int, line.split('|'))) for line in s1.split('\n')]
u = [list(map(int, line.split(','))) for line in s2.split('\n')]

cu, icu = [], []

for up in u:
    im = {p: i for i, p in enumerate(up)}
    valid = True
    for x, y in r:
        if x in im and y in im and im[x] > im[y]:
            valid = False
            break
    if valid:
        cu.append(up)
    else:
        ou = up[:]
        while True:
            ch = False
            for x, y in r:
                if x in ou and y in ou:
                    ix, iy = ou.index(x), ou.index(y)
                    if ix > iy:
                        ou[ix], ou[iy] = ou[iy], ou[ix]
                        ch = True
            if not ch:
                break
        icu.append(ou)

msc = sum(up[len(up) // 2] for up in cu)
msi = sum(up[len(up) // 2] for up in icu)

print(msc)
print(msi)
