// https://leetcode.com/problems/valid-parentheses/
// pop()        to remove last element
// push()       to append to end of list
// [-1]         doesn't work in list so has to be stack.length-1
/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
    var stack = []
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === ")") {
            if (stack[stack.length-1] === "(") {
                stack.pop()
            } else {
                return false;
            }
        } else if (s[i] === "]") {
            if (stack[stack.length-1] === "[") {
                stack.pop();
            } else {
                return false;
            }
        } else if (s[i] === "}") {
            if (stack[stack.length-1] === "{") {
                stack.pop();
            } else {
                return false;
            }
        } else {
            stack.push(s[i]);
        }
    }
    return (stack.length === 0);
};