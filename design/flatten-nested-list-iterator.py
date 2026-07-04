# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]  
    
    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while len(self.stack) > 0:
            top = self.stack[-1]

            if top.isInteger():
                return True
            else:   # if a sub list
                self.stack.pop()    # Remove sublist
                subList = top.getList()

                for i in range(len(subList) - 1, -1, -1):
                    self.stack.append(subList[i])
        
        return False
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
