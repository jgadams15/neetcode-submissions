class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # at each index, check the i+n slots for a number greater than temp[i]
        # append n to the res list.
        # how do we do this in O(n) time complexity?
        # maybe loop through list backwards?
        # how can we use a stack?
        # maybe use the length of the stack at different points
        # for each index i we can push to a stack
        # when a number appears while traversing through array that is greater than i, we return the length of the stack, clear the stack, and continue at i+1
        # how does this handle edge case when no numbers are greater towards end of stack?
        # maybe we pop from list at the start
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t, in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
          
                


            