class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1
        
        # Iterate through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring matches the needle
            if haystack[i:i + len(needle)] == needle:
                return i
        
        return -1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr("hello", "ll"))  # Output: 2
    print(solution.strStr("aaaaa", "bba"))  # Output: -1
    print(solution.strStr("", ""))           # Output: 0
    print(solution.strStr("abc", ""))        # Output: 0
    print(solution.strStr("abc", "d"))       # Output: -1
    print(solution.strStr("abcde", "cde"))   # Output: 2