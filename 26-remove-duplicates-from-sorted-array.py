from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = 0
        for i in range(len(nums) - 1):
            if(nums[i] == nums[i+1]):
                duplicates += 1
                nums[i] = 101
        while(101 in nums):
            nums.remove(101)

        print(duplicates)
        print(len(nums))
x = Solution()
x.removeDuplicates([1,2,3,3,4,5,5,5])



