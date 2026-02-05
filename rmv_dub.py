from typing import List, Tuple


def remove_substrings(strings: List[str]) -> Tuple[List[str], List[str]]:
    seen = set()
    uniq = []
    duplicates = []
    for s in strings:
        if s in seen:
            duplicates.append(s)
        else:
            seen.add(s)
            uniq.append(s)

    uniq_sorted = sorted(uniq, key=len, reverse=True)
    kept = []
    skipped = list(duplicates)
    for i, s in enumerate(uniq_sorted):
        contained = False
        for t in kept:
            if s in t:
                contained = True
                break
        if contained:
            skipped.append(s)
        else:
            kept.append(s)

    kept_set = set(kept)
    kept_in_order = [s for s in uniq if s in kept_set]
    return kept_in_order, skipped
