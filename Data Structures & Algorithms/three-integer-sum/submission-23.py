class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: 
            return []
        
        # Test Case: [-1, 0, 1, 2, -1, 4]
        # -1, 0, 1 and -1, 2, -1 are both valid triplets
        # Sort the array and use converging 2 pointers 
        # nums[i] + nums[left] + nums[right] = 0 
        # nums[left] + nums[right] == -nums[i]

        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1 
            right = len(nums) - 1 

            while left < right: 
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                  triplets.append([nums[i], nums[left], nums[right]])
                  left += 1
                  right -= 1
                  while left < right and nums[left] == nums[left - 1]:
                    left += 1
                    
        return triplets  
                
