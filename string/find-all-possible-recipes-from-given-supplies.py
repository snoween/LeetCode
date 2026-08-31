class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_set = set(recipes)      # get set of recipes to look up later
        graph = defaultdict(list)       # build a graph of each ingredient -> recipe
        in_degree = defaultdict(int)    # build in_degree of each recipe

        for i in range(len(ingredients)):
            unique_ingredients = set(ingredients[i])    # get unique set to avoid +1 in_degree twice
            
            for ingredient in unique_ingredients:
                graph[ingredient].append(recipes[i])
                in_degree[recipes[i]] += 1
 
        queue = deque(supplies)     # queue will store starting points, which are supplies
        ans = []       # ans will store the available recipes

        while queue:
            curr = queue.popleft()      # popleft queue to get current supply
            if curr in recipes_set:     # if curr = recipes -> append to ans
                ans.append(curr)

            for neighbor in graph[curr]:    # loop through all neighbors of that supply
                in_degree[neighbor] -= 1    # decrease the in_degree of that neighbor by 1
                if in_degree[neighbor] == 0:    # append to queue if that in_degree = 0
                    queue.append(neighbor)
        
        return ans