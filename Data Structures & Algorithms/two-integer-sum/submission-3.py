class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        count = 0
        for i in nums :
            diff = target - i
            if diff in d:
                return [d[diff],count]
            else:
                d[i]=count
            count +=1
