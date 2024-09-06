# pytest tests/test_sort_funcs.py

from random import randint

from src.sort_funcs import (gen_bubble_sort, gen_insertion_sort, 
                            gen_merge_sort, gen_quicksort)



class TestSortFuncs:
    nums = [randint(1, 20) for _ in range(10)]
    sorted_nums = sorted(nums)
    sort_funcs = [gen_bubble_sort, gen_insertion_sort, 
                  gen_merge_sort, gen_quicksort]
    
    def test_all_sort_funcs(self):
        for f in self.sort_funcs:
            for i, result in enumerate(f(self.nums)):
                if i == 1000:
                    assert result == self.sorted_nums
                    break 
       