class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    
        s=1
        p = 1
        l = len(nums)
        output = [1]*l
        for i in range(l):
            output[i] = output[i] * p
            p *= nums[i]

        for i in range(l-1,-1,-1):
            output[i]*=s
            s *= nums[i]

        return output