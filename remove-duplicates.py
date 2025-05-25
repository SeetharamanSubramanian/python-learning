class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Initialize a pointer for the next unique element
        unique_index = 0
        
        # Iterate through the list
        for i in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]
        
        # The length of the array with unique elements is unique_index + 1
        return unique_index + 1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1, 1, 2]
    length1 = solution.removeDuplicates(nums1)
    print(length1)  # Output: 2
    print(nums1[:length1])  # Output: [1, 2]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length2 = solution.removeDuplicates(nums2)
    print(length2)  # Output: 5
    print(nums2[:length2])  # Output: [0, 1, 2, 3, 4]

    nums3 = []
    length3 = solution.removeDuplicates(nums3)
    print(length3)  # Output: 0
    print(nums3)    # Output: []