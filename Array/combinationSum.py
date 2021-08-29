#https://leetcode.com/problems/combination-sum/
class Solution(object):
    def combinationSum(self, candidates, target):
        response = []
        self.dfs(candidates, target, [], response)
        return response
             
    def dfs(self, nums, target, path, response):
        if target < 0:
            return 
        if target == 0:
            response.append(path)
            return

        for i in range(0, len(nums)):
            if nums[i] > target:
                continue
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], response) # i: b/c you only want to check sum for combos smaller than that number to prevent duplicates