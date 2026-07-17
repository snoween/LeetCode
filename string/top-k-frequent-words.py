class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = Counter(words)
        heap_freq = []
        output = []

        for key, value in freq.items():
            heapq.heappush(heap_freq, (-value, key))
        
        for i in range(k):
            _, word = heapq.heappop(heap_freq)
            output.append(word)
        
        return output  