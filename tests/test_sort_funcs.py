# pytest tests/test_sort_funcs.py

from random import randint
from src.sort_funcs import bubble_sort

def test_bubble_sort():
    nums = [randint(1, 20)] * 5
    sorted_nums = sorted(nums)
    bubble_sort_results = [bubble_sort(nums)]
    bubble_sorted_nums = bubble_sort_results[-1]
    assert sorted_nums == bubble_sorted_nums