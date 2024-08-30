from typing import Callable, Generator, List, Dict, Tuple


def gen_bubble_sort(A: List[int]) -> Generator:
    A = list(A)
    n = len(A)
    swapped = False
    for _ in range(n-1):
        for i in range(n-1):
            yield A 
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                yield A
                swapped = True
        if not swapped:
            break


def gen_insertion_sort(A: List[int]) -> Generator:
    """basic insertion sort"""
    A = list(A)
    yield A 
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1
            yield A


def gen_merge_sort(A: List[int]) -> Generator:
    A = list(A)
    n = len(A)
    yield A 
    sublist_length = 1 
    while sublist_length <= n:
        # merge all pairs of two sublist of size lenght
        for i in range(0, n, 2*sublist_length): 
            start = i
            middle = i+sublist_length
            end = min(i+2*sublist_length, n)
            sublist_1 = A[start:middle]
            sublist_2 = A[middle:end]
            combined_sorted = _merge(sublist_1, sublist_2)
            # update corresponding part of original list
            A[start:end] = combined_sorted
            yield A
        sublist_length *= 2 


def _merge(A: List[int], B: List[int]) -> List[int]:
    """merge two sorted lists"""
    combined: List[int] = []
    while A and B:
        a = A.pop()
        b = B.pop()
        if a >= b:
            combined.append(a)
            B.append(b)
        else:
            combined.append(b)
            A.append(a)
    leftover = A if A else B
    while leftover:
        combined.append(leftover.pop())
    combined.reverse()
    return combined


def gen_quicksort(A: List[int]) -> Generator:
    A = list(A)
    partition_points: Dict[Tuple[int, int], int] = {}

    def gen_partition(A: List[int], low, high) -> Generator:
        yield A
        pivot = A[high]
        i = low - 1
        for j in range(low, high):
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
                yield A 
        A[i+1], A[high] = A[high], A[i+1]
        yield A
        partition_points[(low, high)] = i+1

    def gen_recur(A: List[int], low, high) -> Generator:
        if low < high:
            yield from gen_partition(A, low, high)
            p = partition_points[((low, high))]
            yield from gen_recur(A, low, p-1)
            yield from gen_recur(A, p+1, high)

    yield from gen_recur(A, 0, len(A) - 1)


def sorting_algorithms() -> List[Callable]:
    return [bubble_sort, 
            gen_insertion_sort, 
            gen_merge_sort, 
            gen_quicksort]
