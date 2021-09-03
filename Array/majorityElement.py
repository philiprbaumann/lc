#https://leetcode.com/problems/majority-element-ii/
# Also known as the Boyer-Moore majority algorithm
# Runs in O(n) time and O(1) space to find x majority components
# The important thing to recognize with this problem is that given we need elements that must be LARGER than N/3 there can only ever
# be a maximum of two elements.
class Solution(object):
    def majorityElement(self, nums):
        count1, count2, cand1, cand2 = 0, 0, 0, 1   # cand1 must be different from cand2

        for n in nums:
            if n == cand1:          # Important thing is to check if n == cand1 or n == cand2 BEFORE we do counts to prevent duplicate nums 
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = n
                count1 += 1
            elif count2 == 0:
                cand2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        return [n for n in (cand1, cand2) if nums.count(n) > len(nums)/3]