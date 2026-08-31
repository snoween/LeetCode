class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_set = set(recipes)
        # build a graph of each ingredient -> recipe
        # build in_degree of each recipe
        graph = defaultdict(list)
        in_degree = defaultdict(int)

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
            # popleft queue to get current supply
            curr = queue.popleft()
            # if curr = recipes -> append to ans
            if curr in recipes_set:
                ans.append(curr)

            # loop through all neighbors of that supply
            for neighbor in graph[curr]:
                # decrease the in_degree of that neighbor by 1
                in_degree[neighbor] -= 1
                # append to queue if that in_degree = 0
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # return ans
        return ans