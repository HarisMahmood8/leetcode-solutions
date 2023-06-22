class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(target <= nums[0]):
            return 0
        for i in range(len(nums)):
            if(nums[i] == target):
                print(i)
                return i
                
            elif(nums[i] > target and nums[i - 1] < target):
                print(i)
                return i
            else:
                continue
        print(len(nums))
        return len(nums)
