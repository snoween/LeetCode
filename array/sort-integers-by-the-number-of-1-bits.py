class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # function to convert int to bin -> str
        def IntToBin(num):
            # define binary_str = ''
            binary_str = ''
            # loop while num > 0
            while num > 0:
                # binary_str = str(num % 2) + binary_str
                binary_str = str(num % 2) + binary_str
            # return binary_str or '0'
            return binary_str or '0'
        
        # create a defaultdict with list
        dictOnes = defaultdict(list)
        # sort arr by heap
        heapq.heapify(arr)
        # while valid heap
        while arr:
            # pop heap arr
            num = heapq.heappop(arr)
            # convert to binary str
            binary_str = IntToBin(num)
            # Make a counter to count its freq
            freq = Counter(binary_str)
            # append the freq of '1' to dict, match with its num
            dictOnes[freq['1']].append(num)
        
        output = []
        # while valid dict
        while dictOnes:
            # get min_key 
            minKey = min(dictOnes)
            # output extend that dict[min_key]
            output.extend(dictOnes[minKey])
            # del min_key
            del dictOnes[minkey]
        
        # return output
        return output