class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        tallest = 0
        while (l < r):
            h = min(height[l], height[r])
            window_size = r - l
            area = h * window_size
            tallest = max(area, tallest)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return tallest

