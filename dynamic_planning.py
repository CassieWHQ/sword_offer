# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small, big = 1, 2
        middle = (tsum + 1) / 2
        ret = []
        while small < middle:
            tmp_sum = sum(range(small, big + 1))
            if tmp_sum < tsum:
                big += 1
            elif tmp_sum > tsum:
                small += 1
            else:
                ret.append(range(small, big + 1))
                big += 1
        return ret

    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return []
        ret = []
        for i in range(len(array)):
            if i == 0 or ret[i - 1] <= 0:
                ret.append(array[i])
            else:
                ret.append(ret[i - 1] + array[i])
        return max(ret)

    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        low = 0
        hight = len(array) - 1

        while low < hight:
            tmp_sum = array[low] + array[hight]
            if tmp_sum > tsum:
                hight -= 1
            elif tmp_sum < tsum:
                low += 1
            else:
                return [array[low], array[hight]]
        return []

sol1=Solution()
print 1,sol1.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2])
print 2,sol1.FindNumbersWithSum([1,2,4,7,11,15],15)
print 3,sol1.FindContinuousSequence(15)
