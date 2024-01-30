class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left_index = 0
        right_index = len(height) - 1

        while (right_index - left_index) != 0:
            if height[left_index] >= height[right_index]:
                max_area = max(height[right_index] * (right_index - left_index), max_area)
                right_index -= 1
            else:
                max_area = max(height[left_index] * (right_index - left_index), max_area)
                left_index += 1
        return max_area


s = Solution()
a = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])

print(a)