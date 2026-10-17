class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = len(strs[0])

        for i in range(1, len(strs)):
            word = strs[i]

            result = min(result, len(word))

            for j in range(result):
                if strs[0][j] != word[j]:
                    result = j
                    break
        
        return strs[0][:result]