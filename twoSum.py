class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            if target - num[i] in dict:
                return (dict[target - num[i]] + 1, i + 1)
            else:
                dict[num[i]] = i