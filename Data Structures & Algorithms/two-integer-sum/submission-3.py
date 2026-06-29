class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}   # value : index 

        for i, num in enumerate(nums):  # enumerate = index : item
            difference = target - num

            if difference in hash: 
                return [hash[difference], i]
            
            hash[num] = i