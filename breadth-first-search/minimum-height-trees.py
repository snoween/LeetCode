class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        graph_reversed = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph_reversed[edge[1]].append(edge[0])
        
        if len(graph) == min(len(graph), len(graph_reversed)):
            return list(graph.keys())
        
        return list(graph_reversed.keys())