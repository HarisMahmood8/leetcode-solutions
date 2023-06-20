class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        indexes = []
        for i in range(1, len(nums) - 1):
            if(nums[i] == nums[i + 1] and nums[i] == nums[i - 1]):
                indexes.append(i)
        for i in indexes:
            nums[i] = "empty"
        while("empty" in nums):
            nums.remove("empty")
            nums.append("_")
        k = 0
        for i in nums:
            if i != "_":
                k += 1
        return k
        
