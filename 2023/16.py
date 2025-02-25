from util import *


def solve(data: str, entry):
    ls = [l.strip() for l in data.splitlines()]
    g = {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}
    visited = set()
    q = deque()
    q.append(entry)
    seen = set()
    while q:
        k = q.popleft()
        if k in seen:
            continue
        seen.add(k)
        p, (dx, dy) = k
        if p not in g:
            continue
        x, y = p
        visited.add(p)

        if g[p] == '.' or (g[p] == '|' and dy == 0) or (g[p] == '-' and dx == 0):
            q.append(((x + dx, y + dy), (dx, dy)))
        elif g[p] == '-' or g[p] == '|':
            q.append(((x - dy, y + dx), (-dy, dx)))
            q.append(((x + dy, y + dx), (dy, dx)))
            q.append(((x + dy, y - dx), (dy, -dx)))
        elif (g[p] == '/' and dx == 0) or (g[p] == '\\' and dy == 0):
            q.append(((x - dy, y + dx), (-dy, dx)))
        else:
            q.append(((x + dy, y - dx), (dy, -dx)))
    return len(visited)


print(solve(D, ((0, 0), (0, 1))))

data = D
xm = len(data.splitlines())
ym = len(data.splitlines()[0])
ans = 0
for j in range(ym):
    ans = max(ans, solve(data, ((0, j), (1, 0))))
    ans = max(ans, solve(data, ((xm - 1, j), (-1, 0))))
for i in range(xm):
    ans = max(ans, solve(data, ((i, 0), (0, 1))))
    ans = max(ans, solve(data, ((i, ym - 1), (0, -1))))
print(ans)
