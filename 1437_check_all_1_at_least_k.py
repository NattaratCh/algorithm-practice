class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastIdx = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if lastIdx != -1:
                    diff = i - lastIdx - 1
                    if diff < k: return False
                lastIdx = i
        return True
