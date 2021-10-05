// https://leetcode.com/problems/sign-of-the-product-of-an-array
/**
 * @param {number[]} nums
 * @return {number}
 */
 var arraySign = function(nums) {
    var ans = 1
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            return 0;
        } else if (nums[i] < 0) {
            ans *= -1
        } 
    }
    return ans;
};