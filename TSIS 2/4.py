class Solution:
    def largestAltitude(self, gain):
        highest = []
        highest.append(0)
        
        for x in gain:
            highest.append(x + highest[-1])
            
        return max(highest)