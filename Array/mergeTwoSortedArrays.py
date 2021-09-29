# https://leetcode.com/problems/merge-sorted-array/
# So this is the solution I came up with off the top of my head and it works, but its intrinsically inefficient as I have to move values over.
# The trick on this one is to avoid that all together by sorting from RIGHT to LEFT instead (or decreasing order).
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return 
        i, j = 0, 0
        while (i < m and j < n):
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                k = m
                while (i < k):
                    nums1[k] = nums1[k-1]
                    k -= 1
                nums1[i] = nums2[j]
                j += 1
                i += 1
                m += 1
        if j != n:
            nums1[i:] = nums2[j:]
                
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
# This is the reversed solution which saves a lot of time.
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while (m > 0 and n > 0):
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        