class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        # If the character is a closing bracket, check if it matches the top of the stack
        # If it is an opening bracket, push it onto the stack
        # Atthe end, the stack should be empty if all brackets are matched correctly

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        return not stack

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))          # Output: True
    print(solution.isValid("()[]{}"))      # Output: True
    print(solution.isValid("(]"))          # Output: False
    print(solution.isValid("([)]"))        # Output: False
    print(solution.isValid("{[]}"))        # Output: True
    print(solution.isValid(""))             # Output: True
    print(solution.isValid("{{{{}}}}"))     # Output: True
    print(solution.isValid("{{{}}}{{{}}}")) # Output: True