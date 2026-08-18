class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        - Algorithm: BFS - stack, no level traversal
        - Time comp: O(M x N)
        - Space comp: O(M x N)
        """
        row, col = len(image), len(image[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()
        set_colors = set((image[sr][sc], color))

        def switchColor(x: int, y: int):
            stack = [(x, y)]
            visited.add((x, y))
            # switch value of box to color value
            image[x][y] = color

            while stack:
                x, y = stack.pop()
                # get neighbor values -> switch color
                for coor in DIRS:
                    newX = x + coor[0]
                    newY = y + coor[1]

                    # check valid box
                    if 0 <= newX < row and 0 <= newY < col and image[newX][newY] in set_colors:
                        if (newX, newY) not in visited:
                            image[newX][newY] = color
                            stack.append((newX, newY))
                            visited.add((newX, newY))
            
            return image
        
        return switchColor(sr, sc)
