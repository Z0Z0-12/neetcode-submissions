class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for t in range(len(temperatures)-1):
            for j in range(t+1, len(temperatures)):
                if temperatures[j] > temperatures[t]:
                    result.append(j-t)
                    break
            
            if len(result) != t+1:
                result.append(0)
        
        result.append(0)

        return result
