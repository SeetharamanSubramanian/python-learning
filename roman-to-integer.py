class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in s:
            current_value = roman_to_int[char]
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value
        
        return total

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))  # Output: 3
    print(solution.romanToInt("IV"))   # Output: 4
    print(solution.romanToInt("IX"))   # Output: 9
    print(solution.romanToInt("LVIII"))  # Output: 58
    print(solution.romanToInt("MCMXCIV"))  # Output: 1994