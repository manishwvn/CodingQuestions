class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = list(strs[0])            
        
        for i in range(1, len(strs)):
            if strs[i] == "":
                    return ''

            for j in range(len(strs[i])):
                print(strs[i]) # a
                
                if len(result) > len(strs[i]):
                    result = result[:len(strs[i])]

                if j >= len(result):  # 0, 2
                    break
                elif result[j] != strs[i][j]: # a,a 

                    result = result[:j]
            print(result)        # [ab]

        return ('').join(result)


        