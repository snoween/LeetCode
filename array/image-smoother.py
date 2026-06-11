class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        img_filter = [[0] * n for _ in range(m)]

        DIRS = [(-1,-1), (-1,0), (-1,1), 
                (0,-1), (0,0), (0,1), 
                (1,-1), (1,0), (1,1)]    # Filter map
        
        for i in range(m):
            for j in range(n):
                neighbors = 0
                count_neighbors = 0
                for di, dj in DIRS:
                    ni = i + di
                    nj = j + dj
                    
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    
                    neighbors += img[ni][nj]   # Get filter map
                    count_neighbors += 1

                img_filter[i][j] = neighbors // count_neighbors      # Apply filter to each cell
        
        return img_filter