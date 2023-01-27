# Print largest common prefix in a list of strings


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # function to find out common prefix between 2 strings 
        def commonPrefixUtil(str1, str2):
            n1 = len(str1)
            n2 = len(str2)
            result = ""
            i = 0
            j = 0

            while i < n1 and j < n2:
                if (str1[i]!= str2[j]):
                    break
                result += str1[i]
                i += 1
                j += 1
            return result

        # finding out the longest common prefix among the list of strings
        prefix = strs[0]
        
        for i in range(1,len(strs)):
            prefix = commonPrefixUtil(prefix, strs[i])
        
        return prefix


#Test Cases:

print(commonPrefixUtil("flower", "flow"))

print(commonPrefixUtil("ab", "a"))

print(commonPrefixUtil("a", ""))



