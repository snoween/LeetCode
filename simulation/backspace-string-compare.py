class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getNextCharacter(s, index):
            backspaceCount = 0

            while index >= 0:
                if s[index] == "#":
                    backspaceCount += 1
                else:
                    if backspaceCount > 0:
                        backspaceCount -= 1
                    else:
                        return (s[index], index)
                index -= 1

            return ("", -1)
            
        i, j = len(s) - 1, len(t) - 1
        while i > 0 or j > 0:
            sChar, i = getNextCharacter(s, i)
            tChar, j = getNextCharacter(t, j)

            if sChar != tChar:
                return False

            i -= 1
            j -= 1

        return True