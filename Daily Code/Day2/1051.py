# 1051. Height Checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        original=heights.copy()
        heights.sort()
        c=0
        for i in range(0,len(heights)):
            if original[i]!=heights[i]:
                c=c+1
        return c