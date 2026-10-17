class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        row = [_ for _ in range(n)]
        col = [_ for _ in range(n, n * 2)]
        diag = [_ for _ in range(n * 2, n * 2 + 2)]

        TIKTOK_MAP = defaultdict(list)

        for i in range(n):
            for j in range(n):
                TIKTOK_MAP[(i, j)] = [row[i], col[j]]

                if i == j:
                    TIKTOK_MAP[(i, j)].append(diag[0])
                
                if i == n-j-1:
                    TIKTOK_MAP[(i, j)].append(diag[1])


        A_TRACK = defaultdict(lambda: 0)
        B_TRACK = defaultdict(lambda: 0)

        for i, move in enumerate(moves):
            if i % 2 == 0:      #Track A 
                pos = TIKTOK_MAP[tuple(move)]
                for num in pos:
                    A_TRACK[num] += 1
                    if A_TRACK[num] == 3:
                        return "A"
                    
            else:   # Track B
                pos = TIKTOK_MAP[tuple(move)]
                for num in pos:
                    B_TRACK[num] += 1
                    if B_TRACK[num] == 3:
                        return "B"

        # Check if Pending                
        if len(moves) != 9:
            return "Pending"

        return "Draw"