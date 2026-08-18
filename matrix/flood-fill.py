class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        - Algorithm: BFS - stack, no level traversal
        - Time comp: O(M x N)
        - Space comp: O(M x N)
        """
        # check if original color = target color -> return image
        original_color = image[sr][sc]
        if original_color == color:
            return image

        row, col = len(image), len(image[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        stack = [(sr, sc)]
        image[sr][sc] = color

        while stack:
            x, y = stack.pop()
            # get neighbor values -> switch color
            for coor in DIRS:
                newX = x + coor[0]
                newY = y + coor[1]

                # check valid box
                if 0 <= newX < row and 0 <= newY < col and image[newX][newY] == original_color:
                    image[newX][newY] = color
                    stack.append((newX, newY))
                 
        return image