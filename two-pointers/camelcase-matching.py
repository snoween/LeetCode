class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        output = []

        for query in queries:
            j = 0
            for char in query:
                if j < len(pattern) and char == pattern[j]:
                    j += 1
                
                elif char.isupper():
                    output.append(False)
                    break

            else:        
                output.append(j == len(pattern))            

        return output