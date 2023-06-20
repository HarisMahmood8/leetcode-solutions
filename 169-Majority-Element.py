from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = dict()

        for i in nums:
            if i not in x:
                x[i] = 1
            else:
                x[i] += 1
            if(x[i] > len(nums)/2):
                return i



x = Solution()
x.majorityElement([3,2,3])
