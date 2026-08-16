class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sort = arr.copy()
        heapq.heapify(arr_sort)
        rank_matching = defaultdict()
        
        rank = 1
        for num in arr:
            num = heapq.heappop(arr_sort)
            if num not in rank_matching:
                rank_matching[num] = rank
                rank += 1
        
        output = []
        for num in arr:
            output.append(rank_matching[num])
        
        return output