class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # {city: bool}
        start_dict = defaultdict(lambda: False)

        for u, v in paths:
            start_dict[u] = True
            start_dict[v]
        
        for city, status in start_dict.items():
            if status == False:
                return city