class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # abbc, abb, abcd

        result = list(strs[0])            
        
        for i in range(1, len(strs)):
            if strs[i] == "":
                    return ''

            for j in range(len(strs[i])):

                # if j >= len(result):  # abcd , ab
                #     break
                if j < len(result) or len(result) > len(strs[i]):
                    result = result[:len(strs[i])]
                else:
                    break     
                
                if result[j] != strs[i][j]: # a,a 
                    result = result[:j]

        return ('').join(result)


        