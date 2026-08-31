class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_set = set(recipes)      # get set of recipes to look up later
        graph = defaultdict(list)       # build a graph of each ingredient -> recipe
        in_degree = defaultdict(int)    # build in_degree of each recipe

        for i in range(len(ingredients)):
            # get unique set of ingredients to avoid increasing the in_degree twice
            unique_ingredients = set(ingredients[i])
            for ingredient in unique_ingredients:
                graph[ingredient].append(recipes[i])
                in_degree[recipes[i]] += 1
 
        # queue will store starting points, which are supplies
        queue = deque(supplies)
        # ans will store the available recipes
        ans = []

        # loop through queue
        while queue:
            curr = queue.popleft()      # popleft queue to get current supply
            
            if curr in recipes_set:     # if curr = recipes -> append to ans
                ans.append(curr)

            # loop through all neighbors of that supply
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1    # decrease the in_degree of that neighbor by 1
                if in_degree[neighbor] == 0:    # append to queue if that in_degree = 0
                    queue.append(neighbor)
        
        # return ans
        return ans