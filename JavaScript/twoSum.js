// https://leetcode.com/problems/two-sum/
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    var visited = {}
    for (var i = 0; i < nums.length; i++) {
        difference = target - nums[i]
        if (difference in visited) {
            return [i, visited[difference]];
        }
        visited[nums[i]] = i;
    }
    return [-1, -1];
};