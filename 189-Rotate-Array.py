from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_end = []
        beginning = 0
        while(beginning <= k):
            new_end.append(nums[beginning])
            beginning += 1
        nums = nums[k+1:] + new_end
        return nums
        

x = Solution()
x.rotate([1,2,3,4,5,6,7],3)
