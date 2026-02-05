from typing import List, Tuple
from overlap import overlap, build_overlap_matrix


def exact_shortest_superstring(strings: List[str]) -> Tuple[str, List[int]]:
    n = len(strings)
    ov = build_overlap_matrix(strings)
    INF = 10**9
    dp = [[INF]*n for _ in range(1<<n)]
    parent = [[-1]*n for _ in range(1<<n)]
    for i in range(n):
        dp[1<<i][i] = len(strings[i])

    for mask in range(1<<n):
        for last in range(n):
            if not (mask & (1<<last)): 
                continue
            cur = dp[mask][last]
            if cur >= INF:
                continue
            for nxt in range(n):
                if mask & (1<<nxt):
                    continue
                added = len(strings[nxt]) - ov[last][nxt]
                nxtmask = mask | (1<<nxt)
                if cur + added < dp[nxtmask][nxt]:
                    dp[nxtmask][nxt] = cur + added
                    parent[nxtmask][nxt] = last

    full = (1<<n) - 1
    best_len = INF
    last = -1
    for i in range(n):
        if dp[full][i] < best_len:
            best_len = dp[full][i]
            last = i

    path = []
    mask = full
    while last != -1:
        path.append(last)
        p = parent[mask][last]
        mask ^= (1<<last)
        last = p
    path = path[::-1]

    if not path:
        return "", []
    res = strings[path[0]]
    for i in range(1, len(path)):
        o = ov[path[i-1]][path[i]]
        res += strings[path[i]][o:]
    return res, path


def build_string_from_order(strings: List[str], order: List[int]) -> str:
    if not order:
        return ""
    res = strings[order[0]]
    for i in range(1, len(order)):
        o = overlap(strings[order[i-1]], strings[order[i]])
        res += strings[order[i]][o:]
    return res


def length_for_order(strings: List[str], order: List[int]) -> int:
    if not order:
        return 0
    total = len(strings[order[0]])
    for i in range(1, len(order)):
        total += len(strings[order[i]]) - overlap(strings[order[i-1]], strings[order[i]])
    return total
