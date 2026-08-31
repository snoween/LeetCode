class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal_node = set()
        for i, edge in enumerate(graph):
            if not edge:
                terminal_node.add(i)
        
        safe_node = []

        for i, edge in enumerate(graph):
            is_path = True
            for ele in edge:
                if ele not in terminal_node:
                    is_path = False
                    break
            
            if is_path:
                safe_node.append(i)
        
        print(safe_node)
        return safe_node