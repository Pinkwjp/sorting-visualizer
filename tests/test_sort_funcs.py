# pytest tests/test_sort_funcs.py

from random import randint

from src.sort_funcs import (gen_bubble_sort, gen_insertion_sort, 
                            gen_merge_sort, gen_quick_sort)



class TestSortFuncs:
    nums = [randint(1, 20) for _ in range(10)]
    sort_funcs = [gen_bubble_sort, gen_insertion_sort, 
                  gen_merge_sort, gen_quick_sort]
    
    def test_all_sort_funcs(self):
        for f in self.sort_funcs:
            results = list(f(numbers=self.nums))
            assert results[-1] == sorted(self.nums)

