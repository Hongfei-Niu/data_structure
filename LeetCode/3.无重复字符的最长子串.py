# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len, left, right = 0, 0, 0
        
        for i in range(len(s)):            
            if s[i] in seen and seen[s[i]] >= left:
                left = seen[s[i]] + 1

            seen[s[i]] = i
            right += 1
            max_len = max(max_len, right - left)
            
        return max_len
        
        
# @lc code=end

