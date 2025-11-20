import random
import time

def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(1, n):
        key = arr[i]
        assignments += 1
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key
        assignments += 1
    return comparisons, assignments

def generate_sequence(n, seq_type):
    if seq_type == 'random':
        return [random.randint(0, n*10) for _ in range(n)]
    elif seq_type == 'ascending':
        return list(range(1, n+1))
    elif seq_type == 'descending':
        return list(range(n, 0, -1))

def main():
    sizes = [10, 100, 1000, 5000, 10000]
    sequence_types = ['random', 'ascending', 'descending']

    type_names = {
        'random': 'Випадкова',
        'ascending': 'Зростаюча',
        'descending': 'Спадна'
    }

    results = []

    for n in sizes:
        for seq_type in sequence_types:
            arr = generate_sequence(n, seq_type)
            arr_copy = arr.copy()

            start_time = time.time()
            comparisons, assignments = insertion_sort(arr_copy)
            end_time = time.time()

            elapsed_time = end_time - start_time

            results.append({
                'size': n,
                'type': seq_type,
                'time_sec': elapsed_time,
                'comparisons': comparisons,
                'assignments': assignments
            })

    print(f"{'N':>6} {'Тип':>12} {'Час (с)':>10} {'Порівняння':>12} {'Присвоєння':>12}")
    print("-" * 70)


    for i, r in enumerate(results):
        print(f"{r['size']:>6} {type_names[r['type']]:>12} {r['time_sec']:>10.6f} "
              f"{r['comparisons']:>12} {r['assignments']:>12}")

        if (i + 1) % 3 == 0:
            print("-" * 70)

if __name__ == "__main__":
    main()
