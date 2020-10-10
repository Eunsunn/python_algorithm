from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        # ### 풀이1 : 재귀 ###
        # if root is None: 
        #     return 0
        # if root.left==root.right==None: # leaf node: depth=1
        #     return 1
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


        ### 풀이2: BFS ###
        # 예외처리
        if root == None or root == "null":
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
    
        return depth


        



