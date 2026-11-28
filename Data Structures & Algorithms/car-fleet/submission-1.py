class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calculate the time it takes for each car to get to the target
        # if time[i] <= time[i+1] then they are in a fleet
        timeStack = []
        cars = sorted(zip(position,speed), reverse = True)
        for pos, spd in cars:
            distance = target - pos
            time = distance / spd
            
            if (len(timeStack) == 0 or time > timeStack[-1]):
                timeStack.append(time)
        return len(timeStack)
        
        