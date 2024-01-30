# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         max_len = 0
#         temp = []
#         for i in s:
#             if i not in temp:
#                 temp.append(i)
#             else:
#                 if len(temp) > max_len:
#                     max_len = len(temp)
#                 temp = [i]
#         return max_len
#
#
# s = Solution()
# print(s.lengthOfLongestSubstring(" "))

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        start = 0
        char_index_map = {}

        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1

            char_index_map[char] = i
            max_len = max(max_len, i - start + 1)

        return max_len

s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))  # Output: 3