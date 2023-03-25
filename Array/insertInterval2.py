# I started off with this trying to figure out the logic for each crossover.
# This is honestly such a pain in the butt and I've gotta notice it right off the bat
# that this can be split up. I had the first part of interval complete. I was having
# issues dealing with the second half.
# Just need to realize that the back half is exactly the same as the front half and go from there.
# The other handy trick here is to recognize that you don't have to build the entire list, but can
# add to separate objects and combine them at the end.

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left, right, start, end = [], [], newInterval[0], newInterval[1]
        for interval in intervals:
            if interval[1] < start:
                left.append(interval)
            elif interval[0] > end:
                right.append(interval)
            else:
                start = min(interval[0], start)
                end = max(interval[1], end)

        return left + [ [start, end] ] + right


# Takeaways:
#   1. Split a problem up into smaller problems. Think from back to front as well as front to back.
#   2. You don't have to build an answer in order, but can combine these answer at the very end.