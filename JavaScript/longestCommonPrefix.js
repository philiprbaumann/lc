// https://leetcode.com/problems/longest-common-prefix/
/**
 * @param {string[]} strs
 * @return {string}
 */
// A ton of edge cases in this code.
 var longestCommonPrefix = function(strs) {
    if (!strs.length) return '';                            // What if strs = ["a"]
    if (!strs[0][0]) return '';                             // What if strs == [""]
    current = strs[0][0]                 
    
    while (true) {
        currLength = current.length
        for (s in strs) {
            if (strs[s].slice(0, currLength) != current) {
                return current.slice(0, currLength-1);
            }
        }
        current = strs[0].slice(0, currLength+1)
        if (current.length == currLength) { return current; }   //  What if strs == ["flow", "flow", "flow"]
    }
};

