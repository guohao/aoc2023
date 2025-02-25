from functools import cache

from util import *


def solve(data: str, ext):
    @cache
    def dfs(paddle, ns):
        if not ns:
            return '#' not in paddle
        if not paddle:
            return 0
        match paddle[0]:
            case '#':
                if '.' in paddle[:ns[0]]:
                    return 0
                if ns[0] == len(paddle) and len(ns) == 1:
                    return 1
                if ns[0] < len(paddle) and paddle[ns[0]] != '#':
                    return dfs(paddle[ns[0] + 1:], ns[1:])
            case '.':
                return dfs(paddle[1:], ns)
            case '?':
                return dfs('#' + paddle[1:], ns) + dfs(paddle[1:], ns)
        return 0

    ss, cgs = data.split()
    cgs = list(map(int, re.findall(r'-?\d+', cgs)))
    return dfs('?'.join([ss] * ext), tuple(cgs) * ext)


t0 = 0
t1 = 0
for l in L:
    t0 += solve(l, 1)
    t1 += solve(l, 5)

print(t0)
print(t1)
