class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # build a graph of each ingredient -> recipe
        # build in_degree of each recipe
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for i in range(len(ingredients)):
            curr_ingredient = ingredients[i]
            for ingredient in curr_ingredient:
                graph[ingredient].append(recipes[i])
                in_degree[recipes[i]] += 1
 
        # queue will store starting points, which are supplies
        queue = deque(supplies)
        # set results will store all nodes in DAG 
        result = set()
        # ans will store the available recipes
        ans = []

        # loop through queue
        while queue:
            # popleft queue to get current supply
            curr = queue.popleft()
            # add that supply to set result
            result.add(curr)

            # loop through all neighbors of that supply
            for neighbor in graph[curr]:
                # decrease the in_degree of that neighbor by 1
                in_degree[neighbor] -= 1

                # append to queue if that in_degree = 0
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # loop through list of ingredients
        for i in range(len(ingredients)):
            curr_ingredient = ingredients[i]
            is_recipe = True

            for ingredient in curr_ingredient:
                # if set(ingredient) in set(results) -> append to ans
                if ingredient not in set(result):
                    is_recipe = False

            if is_recipe:
                ans.append(recipes[i])
                
        # return ans
        return ans