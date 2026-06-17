class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # max area = min(heights[left], [right]) * (right - left)

        max_area = 0 
        for i in range(len(heights)):
            left = i 
            right = len(heights) - 1
            while left < right:
                area = min(heights[left], heights[right]) * (right-left) 
                if area > max_area:
                    max_area = area
                if heights[left] > heights[right]:
                    right -= 1
                else:
                    left += 1
        return max_area

