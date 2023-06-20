class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total_n = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
                total_n -= 1
        while("_" in nums):
            nums.remove("_")
        return total_n
