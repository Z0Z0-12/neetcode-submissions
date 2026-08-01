class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = []

        for i in range(len(temperatures)-1):
            j = i + 1
            greater = 0
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    greater = j - i
                    break
                j += 1
            
            arr.append(greater)
        
        arr.append(0)
        return arr


