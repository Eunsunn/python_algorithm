from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 예외 처리: 빈 순회 리스트
        if len(preorder)==0:
            return None
        
        root = TreeNode(preorder[0])
        root_idx = inorder.index(root.val)
        left_len = root_idx

        left = self.buildTree(preorder[1:1+left_len], inorder[:left_len])
        right = self.buildTree(preorder[1+left_len:], inorder[left_len+1:])

        root.left, root.right = left, right
        return root
