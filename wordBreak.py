ass Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        segmented = [True];
        for i in range (0, len(s)):
            segmented.append(False)
            for j in range(i,-1,-1):
                if segmented[j] and s[j:i+1] in dict:
                    segmented[i+1] = True
                    break
        return segmented[len(s)]

