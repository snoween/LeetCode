class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0

        if name[0] != typed[0]:
            return False
            
        for j in range(len(typed)):
            if i < len(name):
                if name[i] == typed[j]:
                    i += 1
                else:
                    if name[i-1] != typed[j]:
                        return False
                        
            else:   
                if typed[j] != name[i-1]:
                    return False
            
        return i == len(name)