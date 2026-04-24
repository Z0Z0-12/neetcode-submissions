class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        output = []
        word = set()
        for i in range(len(strs)):
            alph = list(strs[i])
            alph.sort()
            if i in word:
                continue           
            element_list = [strs[i]]
            word.add(i)
            for j in range(i+1, len(strs)):
                compare_alph = list(strs[j])
                compare_alph.sort()
                if alph == compare_alph:
                    if j not in word:
                        element_list.append(strs[j])
                        word.add(j)
            output.append(element_list)
        return output
