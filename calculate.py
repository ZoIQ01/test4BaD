from utils import read_numbers
from rmv_dub import remove_substrings
from superstring import exact_shortest_superstring
from search import advanced_local_search


def main():
    path = 'numbers.txt'
    original = read_numbers(path)
    total_read = len(original)
    kept, skipped = remove_substrings(original)
    skipped_count = len(skipped)
    remaining = len(kept)

    print(f"Total strings read: {total_read}")
    print(f"Skipped strings (duplicates or contained in others): {skipped_count}")
    print(f"Remaining strings after cleanup: {remaining}")

    if remaining == 0:
        print("No strings to process.")
        return

    MAX_EXACT = 20
    if remaining <= MAX_EXACT:
        method = "Exact subset DP"
        result, order = exact_shortest_superstring(kept)
    else:
        method = "Advanced local-search (anneal, restarts=50, iterations=10000, seed=0)"
        result, order = advanced_local_search(kept, strategy='anneal', restarts=50, iterations=10000, temp_start=1.0, cooling=0.995, seed=0)

    print(f"Method used: {method}")
    print(f"Result length: {len(result)}")
    print("Resulting superstring:")
    print(result)

    if remaining <= 50:
        print("\nOrder (indices into remaining list):", order)

if __name__ == "__main__":
    main()
