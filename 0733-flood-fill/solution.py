from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        original_image = image[sr][sc]
        if not image:
            return image
        elif original_image == color:
            return image
        rows = len(image)
        cols = len(image[0])
        q = deque([(sr, sc)])
        while q:
            vals = q.popleft()
            r, c = vals[0], vals[1]
            if ((r >= 0) and (r < rows)) and ((c >= 0) and (c < cols)) and image[r][c] == original_image:
                image[r][c] = color
                directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for direction in directions:
                    r, c = direction[0], direction[1]
                    q.append((r, c))
        return image

