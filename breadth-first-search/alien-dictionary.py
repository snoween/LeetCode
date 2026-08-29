class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        in_degree = defaultdict(int)

        # build edge information
        for i in range(len(words) - 1):
            curr_word = words[i]
            next_word = words[i + 1]

            max_len = min(len(curr_word), len(next_word))

            for j in range(max_len):
                if curr_word[j] != next_word[j] and next_word[j] not in adj[curr_word[j]]:
                    adj[curr_word[j]].add(next_word[j])
                    in_degree[next_word[j]] += 1

                    break
        
        queue = deque()
        set_char = set()
        for word in words:
            for char in word:
                set_char.add(char)
        
        for char in set_char:
            if in_degree[char] == 0:
                queue.append(char)
        
        print(queue)
        result = [] 
        while queue:
            curr = queue.popleft()
            result.append(curr)

            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return ''.join(result)