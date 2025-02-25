from util import *


def p1():
    ps = {}
    for line in D.splitlines():
        p, pos = list(map(int, re.findall(r'\d+', line)))
        ps[p] = (pos - 1, 0)
    dc = 0
    dseq = cycle(range(1, 101))
    while True:
        for p, (pos, score) in ps.items():
            moves = sum(next(dseq) for _ in range(3))
            pos = (pos + moves) % 10
            dc += 3
            score += pos + 1
            ps[p] = (pos, score)
            if score >= 1000:
                print(dc * (sum(s for _, s in ps.values()) - score))
                return


ps = {}
for line in D.splitlines():
    p, pos = list(map(int, re.findall(r'\d+', line)))
    ps[p] = pos - 1


def gen_all_moves():
    moves = set()
    for comb in combinations_with_replacement(range(1, 4), 3):
        for x in permutations(comb):
            moves.add(x)
    return moves


def gen_dict(init_pos):
    q = deque()
    d = defaultdict(lambda: defaultdict(int))
    seen = set()
    q.append((init_pos, 1, 0))
    d[0][init_pos, 0] = 1
    while q:
        k = q.popleft()
        if k in seen:
            continue
        seen.add(k)
        pos, t, score = k
        if t not in d:
            d[t] = defaultdict(int)
        for moves in gen_all_moves():
            new_pos = (sum(moves) + pos) % 10
            new_score = score + new_pos + 1
            d[t][new_pos, new_score] += d[t - 1][pos, score]
            if new_score < 21:
                q.append((new_pos, t + 1, new_score))
    ret = defaultdict(lambda: {0: 0, 1: 0})
    for t in d:
        ret[t][1] = sum(times for (_, score), times in d[t].items() if score >= 21)
        ret[t][0] = sum(times for (_, score), times in d[t].items() if score < 21)
    return ret


new_ps = {k: gen_dict(ip) for k, ip in ps.items()}
ans = 0
for i, di in new_ps.items():
    win_times = 0
    for ti, vdi in di.items():
        curr = vdi[1]
        if curr == 0:
            continue
        for oi, doi in new_ps.items():
            if oi == i:
                continue
            if oi < i:
                curr *= doi[ti][0]
            else:
                curr *= doi[ti - 1][0]
        win_times += curr
    ans = max(ans, win_times)
p1()
print(ans)
