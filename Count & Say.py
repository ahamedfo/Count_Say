class Solution(object):
    def countAndSay(self, n):
        num_map = {}
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        strings = "11"
        for i in range(3, n + 1):
            frequency = 1
            build_me = ""
            k = 0
            for i, number in enumerate(strings):
                if i > 0 and number == strings[i - 1]:
                    frequency += 1
                elif i > 0 and number != strings[i - 1]:
                    build_me += (str(frequency) + str(strings[i - 1]))
                    frequency = 1
                if i == len(strings) - 1:
                    build_me += (str(frequency) + str(strings[i]))
            strings = build_me
        return strings