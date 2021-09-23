class Solution:
    def generateParenthesis(self,n:int) -> list:
        root = (n,n,'')
        # root = (0,n,n,'')
        stack = []
        stack.append(root)
        res = []
        while stack:
            # diff,left,right,tmp = stack.pop()
            left,right,tmp = stack.pop()
            if left>right:
                continue
            if left > 0:
                stack.append((left-1,right,tmp+'('))
            if right > 0:
                stack.append((left,right-1,tmp+')'))
            if right == 0 and left == 0:
                res.append(tmp)
        print(res)
Solution().generateParenthesis(3)