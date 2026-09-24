class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        count =0
        for i in nums:
            d[i]=count
            count+=1
        
        for i in range(len(nums)) :
            diff = target - nums[i]
            if diff in nums[i+1:]:
                return [i ,d[diff]]