class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        total = 0      # total net fuel
        tank = 0       # current fuel while scanning
        start = 0      # candidate starting index

        for i in range(n):
            gain = gas[i] - cost[i]
            total += gain
            tank += gain

            # If tank becomes negative, current start fails
            if tank < 0:
                start = i + 1
                tank = 0

        # If total fuel is negative, no solution exists
        if total < 0:
            return -1
        else:
            return start


#my solution

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        flag=1000000
        n=len(gas)
        petrol=0
        index=0
        for i in range (n):
            petrol+=gas[i]
            if petrol<cost[i]:
                petrol=0
                index=i+1
                
            
            else:
                petrol-=cost[i]

        for i in range (index):
            petrol+=gas[i]
            if petrol<cost[i]:
                petrol=0
                flag=0
                    
                
            else:
                petrol-=cost[i]
        if flag==0:
            return -1
        else:
            return index

                        
