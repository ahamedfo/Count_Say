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
                for number in num_map[i-1]:
                    if number not in checker:
                        checker[number] = 1
                    elif number in checker:
                        checker[number] += 1
                    if temp_num != number and temp_num != float("inf"):
                        strings += str(temp_num) * checker[temp_num]
                    temp_num = number
                num_map[i] = int(strings)
        return str


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
temp_number = 0
checker -> 1 = 0
temp_number = 1
