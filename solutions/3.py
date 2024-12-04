import re

testMode = False

example_input = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

data = example_input if testMode else open(__file__.replace('.py', '.in')).read()

data.strip()

p1 = 0
p2 = 0
en = True 
for i in range(len(data)):
    if data[i:].startswith("do()"):
        en = True
    elif data[i:].startswith("don't()"):
        en = False
    ma = re.match(r"mul\((\d+),(\d+)\)", data[i:])
    if ma:
        x, y = map(int, ma.groups())
        p1 += x * y
        if en:
            p2 += x * y

print(p1)
print(p2)
