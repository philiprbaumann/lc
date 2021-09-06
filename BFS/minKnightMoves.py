# I had the right thinking for this: BFS can work, buts its inefficient.
# My line of thinking for optimization was nearly correct...I was thinking along the lines of sectioning off into one quadrant, but came
# up with a case that essentially needs to move outside the quadrant. What I didn't think about was just sectioning off to include this edge
# case instead of just giving up on that line of thinking.

# 
class Solution(object):
    def minKnightMoves(self, x, y):
        queue = [(0,0,0)]
        visited = set([(0,0)])
        x, y = abs(x), abs(y)                                                               # ABS limits our quadrant to the top half of an x,y plane.
        while (queue):
            i, j, step = queue.pop(0)           
            if (i,j)==(x,y): return step                                                    # This is a design pattern that I should remember.
            for it, ij in [(2,1),(2,-1),(-2,1),(1,2),(-1,2),(1,-2)]:                        # No need for (-2,-1) or (-1,-2) as they will never be productive.
                if (i+it,j+ij) not in visited and -1 <= i+it <= x+2 and -1 <= j+ij <= y+2: # This is the limiting that I nearly got. 
                    queue.append((i+it, j+ij, step+1))
                    visited.add( (i+it, j+ij) )
        return -1
                

# The design pattern to remember here, A QUEUE WITH A STEPCOUNT in it. 