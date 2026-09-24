class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d= {}
        for i in nums :
            if i not in d :
                d[i] =1
            else:
                d[i]+=1
        l = sorted(d.items(),key=lambda x:x[1],reverse= True)
        l = [i[0] for i in l[:k]]
        return l