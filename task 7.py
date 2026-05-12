import time
def bubble_sort(arr):
    a = arr.copy()
    comparisons = 0
    swaps = 0
    start = time.time()
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    end = time.time()
    return comparisons, swaps, end - start
def insertion_sort(arr):
    a = arr.copy()
    comparisons = 0
    swaps = 0
    start = time.time()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            comparisons += 1
            a[j + 1] = a[j]
            swaps += 1
            j -= 1
        a[j + 1] = key
    end = time.time()
    return comparisons, swaps, end - start
def quick_sort(a):
    comparisons = [0]
    swaps = [0]
    def partition(low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps[0] += 1
        a[i + 1], a[high] = a[high], a[i + 1]
        swaps[0] += 1
        return i + 1
    def quick(low, high):
        if low < high:
            pi = partition(low, high)
            quick(low, pi - 1)
            quick(pi + 1, high)
    start = time.time()
    quick(0, len(a) - 1)
    end = time.time()
    return comparisons[0], swaps[0], end - start
def merge_sort(arr):
    a = arr.copy()
    comparisons = [0]
    def merge_sort_recursive(a):
        if len(a) > 1:
            mid = len(a) // 2
            left = a[:mid]
            right = a[mid:]

            merge_sort_recursive(left)
            merge_sort_recursive(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                comparisons[0] += 1
                if left[i] < right[j]:
                    a[k] = left[i]
                    i += 1
                else:
                    a[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                a[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                a[k] = right[j]
                j += 1
                k += 1
    start = time.time()
    merge_sort_recursive(a)
    end = time.time()
    swaps = 0
    return comparisons[0], swaps, end - start
data = [64, 34, 25, 12, 22, 11, 90]
bubble = bubble_sort(data)
insertion = insertion_sort(data)
quick = quick_sort(data.copy())
merge = merge_sort(data)
print("Algorithm Comparison")
print("-" * 60)
print("Algorithm\tComparisons\tSwaps\tTime Taken")
print("Bubble Sort\t", bubble[0], "\t\t", bubble[1], "\t", round(bubble[2], 6), "sec")
print("Insertion Sort\t", insertion[0], "\t\t", insertion[1], "\t", round(insertion[2], 6), "sec")
print("Quick Sort\t", quick[0], "\t\t", quick[1], "\t", round(quick[2], 6), "sec")
print("Merge Sort\t", merge[0], "\t\t", merge[1], "\t", round(merge[2], 6), "sec")