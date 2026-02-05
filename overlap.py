from typing import List


def overlap(a: str, b: str) -> int:
    m = min(len(a), len(b))
    for k in range(m, 0, -1):
        if a[-k:] == b[:k]:
            return k
    return 0


def build_overlap_matrix(strings: List[str]) -> List[List[int]]:
    n = len(strings)
    ov = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                ov[i][j] = overlap(strings[i], strings[j])
    return ov
