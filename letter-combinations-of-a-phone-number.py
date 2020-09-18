from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ## 방법1 ##
        # BFS로 문자 하나씩 이어붙이기 (with list comprehension)
        letters = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl",
                "6": "mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if len(digits)==0: return ""
        if len(digits)==1: return letters[digits[0]]

        combination = letters[digits[0]]
        for num in digits[1:]:
            combination = [s+char for char in letters[num] for s in combination]

        return combination


        ## 방법2 ##
        # DFS로 한글자씩 완성하기
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            # digits[index]에 해당하는 모든 문자열 반복
            for j in dic[digits[index]]:
                dfs(index+1, path+j)
        
        # 예외 처리
        if not digits:
            return []

        dic = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl",
                "6": "mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        dfs(0, "")

        return result    






# if __name__ == "__main__":
#     input_string = "23"
#     sol = Solution()
#     print(sol.letterCombinations(input_string))




