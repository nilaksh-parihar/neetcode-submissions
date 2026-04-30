class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1 = [0] * k
        list2 = list(set(nums))
        n = 0
        while k != 0 :
            count = 0
            for i in list2:
                if nums.count(i) > count:
                    count = nums.count(i)
                    list1[n] = i
                    j = i
            n = n+1
            k = k-1
            list2.remove(j)
        
        return list1

