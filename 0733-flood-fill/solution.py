from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if not image:
            return image
        rows, cols = len(image), len(image[0])
        orig = image[sr][sc]
        if orig == color:
            return image
        q = deque([(sr, sc)])
        image[sr][sc] = color
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == orig:
                    image[nr][nc] = color
                    q.append((nr, nc))
        return image


