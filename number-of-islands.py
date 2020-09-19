from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #########################################
        ##                 BFS                 ##
        #########################################

        xdir = [1, -1, 0, 0]
        ydir = [0, 0, 1, -1]
        cnt = 0 # the number of BFS start point

        # Initialized visited list (0-> True, 1->False)
        if len(grid)==0: return cnt
        row, col = len(grid), len(grid[0])
        visited = []
        for i in range(row):
            visited.append([grid[i][j]=='0' for j in range(col)])

        # return (row, col)
        def find_start():
            for i in range(row):
                for j in range(col):
                    if not visited[i][j]:
                        return (i,j)
            return (-1, -1)

        
        queue = collections.deque()
        cur_y, cur_x = find_start()
        
        # For start point
        while cur_y != -1:
            visited[cur_y][cur_x] = True
            queue.append((cur_y, cur_x))
            cnt += 1
            # BFS
            while queue:
                cur_y, cur_x = queue.popleft()
                for idx in range(len(xdir)):
                    tmp_y, tmp_x = cur_y+ydir[idx], cur_x+xdir[idx]
                    if tmp_x >=col or tmp_x < 0 or tmp_y>=row or tmp_y<0: continue
                    if not visited[tmp_y][tmp_x]: 
                        queue.append((tmp_y, tmp_x))
                        visited[tmp_y][tmp_x] = True

            # Find next start point
            cur_y, cur_x = find_start()

        return cnt







        #########################################
        ##          Recursive  DFS             ##
        #########################################

        xdir = [1, -1, 0, 0]
        ydir = [0, 0, 1, -1]
        cnt = 0
        
        # Empty list
        if len(grid)==0: return cnt
        
        row, col = len(grid), len(grid[0])
        visited = [[grid[i][j]=='0' for j in range(col)]for i in range(row)]

        # return (row, col)
        def find_start():
            for i in range(row):
                for j in range(col):
                    if not visited[i][j]:
                        return (i,j)
            return (-1, -1)


        # recursive DFS
        def dfs(y, x):
            for i in range(len(xdir)):
                tmp_y, tmp_x = y+ydir[i], x+xdir[i]
                # 인덱스 벗어나거나, 이미 방문한 경우 예외처리
                if tmp_y < 0 or tmp_y >= row or tmp_x < 0 or tmp_x >= col: continue
                if visited[tmp_y][tmp_x]: continue
                # 방문하지 않은 곳에서 DFS한다
                visited[tmp_y][tmp_x] = True
                dfs(tmp_y, tmp_x)


        cur_y, cur_x = find_start()

        while cur_y != -1:
            # 시작점을 방문표시한다 : 시작점마다 +1
            visited[cur_y][cur_x] = True
            cnt += 1
            # 현재 시작점에서 DFS 탐색 -> visited 갱신
            dfs(cur_y, cur_x)
            # 다음 시작점을 갱신
            cur_y, cur_x = find_start()

            
        return cnt








        #########################################
        ##          Iterative  DFS             ##
        #########################################

        xdir = [1, -1, 0, 0]
        ydir = [0, 0, 1, -1]
        cnt = 0
        
        if len(grid)==0: return cnt
        row, col = len(grid), len(grid[0])
        visited = [[grid[i][j]=='0' for j in range(col)] for i in range(row)]

        # return (row, col)
        def find_start():
            for i in range(row):
                for j in range(col):
                    if not visited[i][j]:
                        return (i,j)
            return (-1, -1)


        cur_y, cur_x = find_start()

        while cur_y != -1:
            visited[cur_y][cur_x] = True
            stack = [(cur_y, cur_x)]
            cnt += 1
            # DFS
            while stack:
                cur_y, cur_x = stack.pop()
                for i in range(len(ydir)):
                    tmp_y, tmp_x = cur_y+ydir[i], cur_x+xdir[i]
                    if tmp_y < 0 or tmp_y >= row or tmp_x < 0 or tmp_x >= col: continue
                    if visited[tmp_y][tmp_x]: continue
                    stack.append((tmp_y, tmp_x))
                    visited[tmp_y][tmp_x] = True
            # Find next start point
            cur_y, cur_x = find_start()

        return cnt






# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
sol = Solution()
print(sol.numIslands(grid))