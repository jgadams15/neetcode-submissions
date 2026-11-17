class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadyExist = []
        for num in nums:
            if(num in alreadyExist):
                return True
            alreadyExist.append(num)
        return False