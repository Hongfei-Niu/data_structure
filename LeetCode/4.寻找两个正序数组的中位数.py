#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n = len(nums1) + len(nums2)
        
        left, right = 0, 0
        ifsing = n % 2
        
        for i in range(n):
            if nums1[left] < nums2[right]:
                tmp = nums1[left]
                left += 1
                
            else:
                tmp = nums1[left]
                right += 1
                
            if n % 2:
                if i in [n / 2, n / 2 - 1]:
                    output += tmp
            
                elif i > n / 2:
                    return output
                
            else:
                if i == n // 2:
                    return tmp
# @lc code=end