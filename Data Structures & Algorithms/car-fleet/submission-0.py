class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        newList = [(position[i], speed[i]) for i in range(len(position))]
        newList.sort(reverse=True)

        stack = []
        fleetCount = 0

        for i in range(len(newList)):
            currPos, currSpeed = newList[i]
            currTime = (target-currPos) / currSpeed

            if not stack or currTime > stack[-1]:
                stack.append(currTime)
            
        return len(stack)
            
