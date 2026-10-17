class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        # 10 leds
        leds = [(8, 'h'), (4, 'h'), (2, 'h'), (1, 'h'), 
                (32, 'm'), (16, 'm'), (8, 'm'), (4, 'm'), (2, 'm'), (1, 'm')]
        
        result = []
        def backtrack(start_idx, num_leds, curr_h, curr_m):
            # 3. pruning
            if curr_h >= 12 or curr_m >= 60:
                return
            
            # 1. base case
            if num_leds == turnedOn:
                time = f"{curr_h}:{curr_m:02d}"     # h:mm
                result.append(time)
                return
            
            # 2. get combinations
            for i in range(start_idx, 10):
                val, typ = leds[i]

                if typ == 'h':
                    curr_h += val
                else:
                    curr_m += val

                backtrack(i + 1, num_leds + 1, curr_h, curr_m)

                # undo
                if typ == 'h':
                    curr_h -= val
                else:
                    curr_m -= val
        
        backtrack(0, 0, 0, 0)
        return result