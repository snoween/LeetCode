class Solution:
    def simplifyPath(self, path: str) -> str:
        element_list = path.split('/')
        output_path = []

        for ele in element_list:
            if ele == '' or ele == '.': # .. != '', . != ''
                continue
            if ele == '..':
                if output_path:
                    output_path.pop()
                continue
            output_path.append(ele)
        
        return '/' + '/'.join(output_path)
                