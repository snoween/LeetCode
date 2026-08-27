class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        - Idea: sort input -> append if interval[0] > last interval[1]
        Update end if interval[0] < last interval[1]
        - Time comp: O(N)
        - Space comp: O(N)
        """
        # sort input
        intervals.sort(key = lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
        
        return merged