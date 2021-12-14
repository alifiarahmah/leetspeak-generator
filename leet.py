# main program for leetspeak translator

from leetdict import d
from prng import LCG

s = input()

idx = []
result = ""

for i in range(len(s)):
    if s[i] != ' ':
        idx = LCG(i, len(d[s[i]]))
        result += d[s[i].lower()][idx]
    else:
        result += ' '

print(result)
