class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        char_freq = []
        for key, value in freq.items():
            char_freq.append((-value, key))
        
        heapq.heapify(char_freq)
        output = []
        while char_freq:
            element = heapq.heappop(char_freq)
            output.append(element[1] * (-element[0]))
        
        return ''.join(output)