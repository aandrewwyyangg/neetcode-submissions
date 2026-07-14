class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # find the first index where the cost is positive
        # start looping? 


        # Initialize variables total, tank, and start to 0
        # Loop through the length of the gas stations

        total = 0   # running sum of every station
        tank = 0    # current fuel
        start = 0   # current best guess

        for i in range(len(gas)): 
            diff = gas[i] - cost[i] # this is the "net" for this station
            tank += diff 
            total += diff 

            if tank < 0: 
                start = i + 1
                tank = 0
            
        if total < 0: 
            return -1

        return start