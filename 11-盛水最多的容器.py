class Solution:
    def maxArea(self, height: list) -> int:
        head = 0
        tail = len(height) - 1
        max_area = 0
        while head < tail:
            tmp_area = (tail - head)*min(height[head],height[tail])
            if tmp_area > max_area:
                max_area = tmp_area
            if height[head] > height[tail]:
                tail -= 1
            else:
                head += 1

        return max_area

a = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(a)