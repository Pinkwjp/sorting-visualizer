# pytest tests/test_sort_funcs.py

from random import randint
from typing import List

from src.sort_funcs import (gen_bubble_sort, gen_insertion_sort, 
                            gen_merge_sort, gen_quicksort)



def final_sorted_result(sort_func, nums) -> List[int]:
    partial_sorted_results = [partial_result for partial_result in sort_func(nums)]
    final_result = partial_sorted_results[-1]
    return final_result


class TestSortFuncs:
    nums = [randint(1, 20) for _ in range(10)]
    sorted_nums = sorted(nums)
    sort_funcs = [gen_bubble_sort, gen_insertion_sort, gen_merge_sort, gen_quicksort]

    def test_all_sort_funcs(self):
        for f in self.sort_funcs:
            assert final_sorted_result(f, self.nums) == self.sorted_nums