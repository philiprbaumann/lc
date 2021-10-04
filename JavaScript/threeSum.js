// https://leetcode.com/problems/3sum/
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
// This is a hard question.
// Core logic is as follows: Iterate over from 0 to len(n)-1 where this value is the current "base".
// We then compare this base to the left and right iterators (l == i + 1, r == endOfNums) and try and make them add up to 0
// The hard part is the skipping of duplicate values (which occurs for i, l and r at separate points in the code)
// Also, don't forget --; and ++;. 
 var threeSum = function(nums) {
    nums.sort((a, b) => a - b);         // This is also a tricky thing. Sort automatically works lexicographically. 
    answer = []                         // By passing, (a,b)=>a-b we're sorting in ascending order. (a,b)=> b-a is descending. 
    
    for (let i = 0; i < nums.length-2; i++) {
        if (i > 0 && nums[i] === nums[i-1]) { continue }
        l = i + 1
        r = nums.length - 1
        while (l < r) {
            currSum = nums[l] + nums[r] + nums[i]
            if ( currSum > 0 ) {
                r--;
            } else if (currSum < 0 ) {
                l++;
            } else {
                answer.push([ nums[l], nums[r], nums[i] ]);
                while (l < r && nums[l] === nums[l+1]) {
                    l++;   
                }
                while (l < r && nums[r] === nums[r-1]) {
                    r--;
                }
                l++;
                r--;
            }
        }
    }
    return answer;
};