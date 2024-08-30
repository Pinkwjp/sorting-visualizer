# pytest tests/test_sort_funcs.py

from random import randint
from src.sort_funcs import bubble_sort

def test_bubble_sort():
    nums = [randint(1, 20) for _ in range(5)]
    bubble_sort_results = [partial_result for partial_result in bubble_sort(nums)]
    bubble_sorted_nums = bubble_sort_results[-1]
    assert bubble_sorted_nums == sorted(nums)