class Solution:
    def intToRoman(self, num: int) -> str:
        # Define a list of tuples containing Roman numeral symbols and their corresponding values
        val = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        # Initialize the result string
        roman_numeral = ""

        # Loop through each symbol, subtracting its value from the number and appending the symbol to the result
        for (value, symbol) in val:
            while num >= value:
                roman_numeral += symbol
                num -= value

        return roman_numeral

# Example usage:
sol = Solution()
print(sol.intToRoman(9))      # Output: IX
print(sol.intToRoman(58))     # Output: LVIII
print(sol.intToRoman(1994))   # Output: MCMXCIV
