class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # key = content, value = list(files)
        file_content = defaultdict(list)

        # get file name and its content
        for path in paths:
            parts = path.split(' ')
            directory = parts[0]

            for i in range(1, len(parts)):
                file_info = parts[i].split('(')
                file_name = file_info[0]            
                content = file_info[1][:-1]        
                
                full_path = directory + "/" + file_name
                file_content[content].append(full_path)
        
        results = []

        for value in file_content.values():
            results.append(value)
        
        return results
