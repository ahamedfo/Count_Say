class Solution(object):
    def countAndSay(self, n):
        num_map = {}
        strings = ""
        for i in range(1, n):
            checker = {}
            if i == 1:
                num_map = 1
            else:
                temp_num = float("inf")
                for number in num_map[i]:
                    if number not in checker:
                        checker[number] = 0
                    elif number in checker:
                        checker[number] += 1
                    if checker[number] > 0 and temp_num != number:
                        strings += str(number) * checker[number]
                    temp_num = number


        """
        :type n: int
        :rtype: str
        """

1 -> 1
2 -> 11
3 -> 21
4 -> 1211
5 -> 111221
6 -> 312211

1 = 1
2 = 1 + 10
3 = 10 + 11
4 =