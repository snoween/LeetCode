class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        - Algorithm: DFS
        - Time comp: O(M x N)
        - Space comp: O(M x N)
        """
        # check if original color = target color -> return image
        originalColor = image[sr][sc]
        if originalColor == color:
            return image

        row, col = len(image), len(image[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        stack = [(sr, sc)]
        image[sr][sc] = color

        while stack:
            x, y = stack.pop()
            # get neighbor values -> switch color
            for dx, dy in DIRS:
                newX = x + dx
                newY = y + dy

                # check valid box
                if not(0 <= newX < row and 0 <= newY < col):
                    continue
                if image[newX][newY] != originalColor:
                    continue
                    
                image[newX][newY] = color
                stack.append((newX, newY))
                 
        return image