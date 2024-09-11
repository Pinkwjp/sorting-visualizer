
from copy import deepcopy
from typing import Generator, List, Dict, Tuple


def gen_bubble_sort(A: List[int]) -> Generator:
    A = list(A)
    yield A 
    n = len(A)
    swapped = False
    for _ in range(n-1):
        for i in range(n-1):
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
            before_merge = deepcopy(A[start:end])
            sublist_1 = A[start:middle]
            sublist_2 = A[middle:end]
            combined_sorted = _merge(sublist_1, sublist_2)
            # update corresponding part of original list
            A[start:end] = combined_sorted
            # check if swap happened
            for a, b in zip(before_merge, combined_sorted):
                if a != b:  
                    yield A 
                    break
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




def gen_merge_sort_with_more_yield(A: List[int]) -> Generator:
    """yield more partially sorted sequences"""
    A = list(A)
    sorted_A = sorted(A)
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

            partial_sequence = deepcopy(A[start:end])
            full_sequence = deepcopy(A)

            for sequence in _merge_with_more_yield(sublist_1, sublist_2):
                for a, b in zip(sequence, partial_sequence):
                    if a != b:       
                        partial_sequence = sequence
                        full_sequence[start:end] = sequence
                        yield full_sequence
                        break
            A[start:end] = partial_sequence
        sublist_length *= 2 


def _merge_with_more_yield(A: List[int], B: List[int]) -> Generator:
    """merge two sorted lists, yield more partially sorted sequences"""
    # reverse from large to small for pop
    A = list(reversed(A))  
    B = list(reversed(B))
    combined: List[int] = [] # small to large
    while A and B:
        a = A.pop()
        b = B.pop()
        # pick the smaller one 
        if a <= b:
            combined.append(a)
            B.append(b)
            if B and (not A):
                yield list(combined + list(reversed(B)))
        else:
            combined.append(b)
            A.append(a)
            # yield every partially sorted sequence
            yield  list(combined 
                        + list(reversed(A)) 
                        + list(reversed(B))) 




# FIXME: too much yield
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



def k_gen_quicksort(A: List[int]) -> Generator:
    A = list(A)
    partition_points: Dict[Tuple[int, int], int] = {}

    def gen_partition(A: List[int], low, high) -> Generator:
        # yield A
        pivot = A[high]
        i = low - 1
        for j in range(low, high):
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
                if A[i] != A[j]:  # reduce duplicate yield
                    yield A 
        A[i+1], A[high] = A[high], A[i+1]
        if A[i+1] != A[high]:  # reduce duplicate yield
            yield A
        partition_points[(low, high)] = i+1

    def gen_recur(A: List[int], low, high) -> Generator:
        if low == 0 and high == len(A) -1:  # yield initial sequence
            yield A

        if low < high:
            yield from gen_partition(A, low, high)
            p = partition_points[((low, high))]
            yield from gen_recur(A, low, p-1)
            yield from gen_recur(A, p+1, high)

    yield from gen_recur(A, 0, len(A) - 1)





def x_gen_quicksort(A: List[int]) -> Generator:
    A = list(A)
    partition_points: Dict[Tuple[int, int], int] = {}

    def gen_partition(A: List[int], low, high) -> Generator:
        # yield A
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
    
    # TODO: put this in a decorator to filter repeated sequences
    yield A
    unique_results = set(tuple(A))
    for a in gen_recur(A, 0, len(A) - 1):
        if tuple(a) not in unique_results:
            unique_results.add(tuple(a))
            yield a




