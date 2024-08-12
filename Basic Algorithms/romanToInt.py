class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        n = len(s)

        def value(ch):
            if ch == 'I':
                return 1
            elif ch == 'V':
                return 5
            elif ch == 'X':
                return 10
            elif ch == 'L':
                return 50
            elif ch == 'C':
                return 100
            elif ch == 'D':
                return 500
            elif ch == 'M':
                return 1000  
            else:
                return -1

        i = 0
        while i < n:
            s1 = value(s[i])

            if (i + 1) < n:
                s2 = value(s[i + 1])
                if s1 >= s2:
                    res += s1
                else:
                    res += s2 - s1
                    i += 1  # Skip the next character
            else:
                res += s1
            i += 1  # Always increment i at the end of the loop
        return res



if __name__ == "__main__":

    # Example usage:
    sol = Solution()
    print(sol.romanToInt("IX"))    # Output: 9
    print(sol.romanToInt("LVIII")) # Output: 58
    print(sol.romanToInt("MCMXCIV")) # Output: 1994
