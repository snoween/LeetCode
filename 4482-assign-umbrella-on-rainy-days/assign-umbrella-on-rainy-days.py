class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        """
        If rain[i] = rain[i + 1] = 1 -> append 'Alice'
        If rain[i] = 1 -> append 'Bob'
        If rain[i] = 0 -> append ' None'
        [1 1 1 1] -> [Alice Bob Alice Bob]
        - Manage count umbrella for Alice and Bob
        """
        count_Alice = 0
        count_Bob = 0
        n = len(rain)
        result = []
        
        for i, curr_day in enumerate(rain):
            if i < n - 1 and curr_day == rain[i + 1] == 1:
                if count_Alice <= count_Bob:
                    result.append('Alice')
                    count_Alice += 1
                else:
                    result.append('Bob')
                    count_Bob += 1
            elif curr_day == 1:
                result.append('Bob')
                count_Bob += 1
            else:
                result.append('None')

        return result
                