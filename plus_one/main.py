class Solution(object):

    def plusOne(self, digits):
        final = 0
        for i in range(len(digits)):
            final += digits[i] * (10 ** (len(digits) - 1 - i))

        ret = []
        final += 1
        while final > 0:
            ret.insert(0, final % 10)
            final = final // 10
        return ret
        """
        :type digits: List[int]
        :rtype: List[int]
        """


if __name__ == '__main__':
    c = Solution()
    digits = [1, 2, 3]
    print(c.plusOne(digits))
