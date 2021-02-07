# naive.py

s = 'Mississippi'

d = dict()
for k in s:
    if k in d:
        d[k] += 1
    else:
        d[k] = 1

print(d.items())

