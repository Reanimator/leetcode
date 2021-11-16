# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        result = 0
        for pos, sym in enumerate(s):
            result += self.roman_dict[sym]
            if (sym == 'V' or sym == 'X') and pos != 0 and s[pos-1] == 'I':
                result -= 2
            if (sym == 'L' or sym == 'C') and pos != 0 and s[pos-1] == 'X':
                result -= 20
            if (sym == 'D' or sym == 'M') and pos != 0 and s[pos - 1] == 'C':
                result -= 200
        return result


if __name__ == "__main__":
    print(Solution().romanToInt(s="III"))
    print(Solution().romanToInt(s="IV"))
    print(Solution().romanToInt(s="IX"))
    print(Solution().romanToInt(s="LVIII"))
    print(Solution().romanToInt(s="MCMXCIV"))
    print(Solution().romanToInt(s="MMMCDXC"))
    print(Solution().romanToInt(s="VII"))




