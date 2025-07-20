# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        ans=[]
        q= deque([root])
        while q :
            level_node =[]
            leng = len(q)
            for i in range(leng):
                nod=q.popleft()
                level_node.append(nod.val)
                if nod.left:
                    q.append(nod.left)
                if nod.right:
                    q.append(nod.right)
            ans.append(level_node)
        return ans      
                    

