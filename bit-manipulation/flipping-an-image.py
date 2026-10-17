class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        # Reverse each row
        for i, row in enumerate(image):
            row[::-1] = row[::1]
        
        # Invert image
        for i in range(n):
            for j in range(n):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1

        return image