class Solution(object):
    def countAndSay(self, n):
        num_map = {}
        for i in range(0, n):
            if i == 1:
                num_map = 1
            else:
                num_map[i] = num_map[i - 1]
        """
        :type n: int
        :rtype: str
        """

1 -> 1
2 -> 11
3 -> 21
4 -> 1211