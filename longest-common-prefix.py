class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for s in strs[1:]:
            while not s.startswith(prefix):
                # Shorten the prefix until it matches
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))    # Output: ""
    print(solution.longestCommonPrefix([""]))                        # Output: ""
    print(solution.longestCommonPrefix(["a"]))                       # Output: "a"
    print(solution.longestCommonPrefix(["ab", "a"]))                 # Output: "a"