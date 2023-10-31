class Solution:
    def romanToInt(self, s: str) -> int:
        vals = { "I" : 1,
                 "V" : 5,
                 "X" : 10,
                 "L" : 50,
                 "C" : 100,
                 "D" : 500,
                 "M" : 1000}
        sum = 0
        for i in range(len(s)):
            if (i == 0):
                sum += vals[s[i]]
            # This is the essential condition, which checks if the current value is greater than previous value, 
            # if so we need to remove the previous value and then do newVal - prevVal, so we get newVal - 2*prevVal  
            elif (vals[s[i]] > vals[s[i - 1]]): 
                sum += vals[s[i]] - 2*vals[s[i-1]]

            else:
                sum += vals[s[i]]
            
        return sum
