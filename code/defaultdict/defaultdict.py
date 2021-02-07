from collections import defaultdict

s = 'Mississippi'

d = defaultdict(int)
for k in s:
    d[k] += 1

print(d.items())

