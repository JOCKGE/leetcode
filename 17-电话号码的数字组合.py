class Solution:
    def letterCombinations(self,digits: str):
        if not digits:
            return []
        stack = [(0,'','')]
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # stack += list(phone_map[digits[0]])
        res = []
        while len(stack) != 0:
            step, s , tmp_res= stack.pop()
            # if node < len(digits)-1:
            #     stack += list((node+1,phone_map[digits[node]]))
            if step < len(digits):
                string_list_next = list(phone_map[digits[step]])
                for st in string_list_next:
                    stack.append((step+1,st,tmp_res+st))
            else:
                # print(tmp_res)
                res.append(tmp_res)
        return res


a = Solution().letterCombinations('')
print(a)