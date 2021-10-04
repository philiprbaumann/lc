// https://leetcode.com/problems/palindrome-number/
/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    if (x<0) { return false; }
    x = x.toString()  // This is actually pretty inefficient casting to String. 
    i = 0, j = x.length-1
    while (i < j) {
        if (x[i] != x[j]) {
            return false;
        }
        i += 1;
        j -= 1;
    }
    
    return true;
};

// This is significantly quicker:
/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    if (x<0) { return false; }
    x = x+''        // Casting by appending an empty char is much quicker. 
    i = 0, j = x.length-1
    while (i < j) {
        if (x[i] != x[j]) {
            return false;
        }
        i += 1;
        j -= 1;
    }
    
    return true;
};