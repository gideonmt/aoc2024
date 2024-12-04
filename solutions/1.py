from collections import Counter

testMode = False

example_input = """
3 4
4 3
2 5
1 3
3 9
3 3
"""

data = example_input if testMode else open(__file__.replace('.py', '.in')).read()

lines = data.strip().split('\n')

ll = []
rl = []
for line in lines:
    l, r = map(int, line.split())
    ll.append(l)
    rl.append(r)

ll.sort()
rl.sort()

td = sum(abs(l - r) for l, r in zip(ll, rl))

print(td)

rlc = Counter(rl)

ss = sum(num * rlc[num] for num in ll)

print(ss)
