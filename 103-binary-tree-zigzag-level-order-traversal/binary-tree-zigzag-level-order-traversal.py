# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=deque()
        res=[]
        queue.append(root)
        counter=0
        while queue:
            size=len(queue)
            level=[]
            for _ in range(size):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if counter%2==0:
                res.append(level)
            else:
                res.append(level[::-1])
            counter+=1
        return res
                    

        