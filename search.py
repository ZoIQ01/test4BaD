from typing import List, Tuple
import random
from overlap import build_overlap_matrix
from superstring import build_string_from_order


def advanced_local_search(strings: List[str], strategy: str = 'anneal', restarts: int = 50, iterations: int = 10000, temp_start: float = 1.0, cooling: float = 0.995, seed: int = None) -> Tuple[str, List[int]]:
    n = len(strings)
    if n == 1:
        return strings[0], [0]

    rnd = random.Random(seed)
    indices = list(range(n))

    ov = build_overlap_matrix(strings)

    def order_length(order: List[int]) -> int:
        total = len(strings[order[0]])
        for k in range(1, n):
            total += len(strings[order[k]]) - ov[order[k-1]][order[k]]
        return total

    def random_swap(order: List[int]):
        i = rnd.randrange(0, n)
        j = rnd.randrange(0, n)
        if i == j:
            return order
        order[i], order[j] = order[j], order[i]
        return order

    def random_insert(order: List[int]):
        i = rnd.randrange(0, n)
        j = rnd.randrange(0, n)
        if i == j:
            return order
        x = order.pop(i)
        order.insert(j, x)
        return order

    def random_two_opt(order: List[int]):
        i = rnd.randrange(0, n-1)
        j = rnd.randrange(i+1, n)
        order[i:j+1] = reversed(order[i:j+1])
        return order

    def neighbor(order: List[int], strat: str):
        new = order[:]
        if strat == 'swap':
            return random_swap(new)
        elif strat == 'insert':
            return random_insert(new)
        elif strat == 'two-opt':
            return random_two_opt(new)
        else:  # mix
            choice = rnd.choice(['swap', 'insert', 'two-opt'])
            return neighbor(new, choice)

    best_order = sorted(indices, key=lambda i: -len(strings[i]))
    best_len = order_length(best_order)

    for r in range(restarts):
        if r == 0:
            order = best_order[:]
        else:
            order = indices[:]
            rnd.shuffle(order)

        cur_order = order[:]
        cur_len = order_length(cur_order)
        best_local_order = cur_order[:]
        best_local_len = cur_len

        if strategy == 'anneal':
            T = temp_start
            for it in range(iterations):
                new_order = neighbor(cur_order, 'mix')
                new_len = order_length(new_order)
                d = new_len - cur_len
                if d <= 0 or rnd.random() < min(1.0, pow(2.718281828, -d / max(1e-12, T))):
                    cur_order = new_order
                    cur_len = new_len
                    if cur_len < best_local_len:
                        best_local_len = cur_len
                        best_local_order = cur_order[:]
                T *= cooling
        else:
            changed = True
            it = 0
            while it < iterations and changed:
                changed = False
                for _ in range(n*2):
                    new_order = neighbor(cur_order, strategy)
                    new_len = order_length(new_order)
                    if new_len < cur_len:
                        cur_order = new_order
                        cur_len = new_len
                        changed = True
                it += 1
            best_local_order = cur_order[:]
            best_local_len = cur_len

        if best_local_len < best_len:
            best_len = best_local_len
            best_order = best_local_order[:]

    result_str = build_string_from_order(strings, best_order)
    return result_str, best_order


def permutation_local_search(strings: List[str], restarts: int = 50, max_no_improve: int = 500) -> Tuple[str, List[int]]:
    return advanced_local_search(strings, strategy='swap', restarts=restarts, iterations=max_no_improve, seed=None)
