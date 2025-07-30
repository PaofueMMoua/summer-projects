class Solution:
    def slowestKey(self, releaseTimes: [int], keysPressed: str) -> str:
        # loop through the keys time
        tempLongTime = 0
        tempIndex = ''
        for index in range(len(releaseTimes)):
            if index == 0:
                currTime = releaseTimes[index] 
            else:
                currTime = releaseTimes[index] - (releaseTimes[index-1])
            if currTime >= tempLongTime:
                if currTime == tempLongTime:
                    
                tempLongTime = currTime
                tempIndex = keysPressed[index]
            print('currtime')
            print(currTime)
            print()
            print('templongtime')
            print(tempLongTime)
            print()
            print('tempindex')
            print(tempIndex)
            print()

        return tempIndex

        # take the key time and compare it to the last one and the biggest difference is the answer.


releaseTimes = [1,2]
keysPressed = "ba"

response = Solution().slowestKey(releaseTimes, keysPressed)

print()
print()
print()
print()
print(response)