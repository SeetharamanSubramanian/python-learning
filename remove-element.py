from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        # Initialize a pointer for the next position to fill
        position = 0
        
        # Iterate through the list
        for i in range(len(nums)):
            # If the current element is not equal to val, keep it
            if nums[i] != val:
                nums[position] = nums[i]
                position += 1
        
        # The length of the array with elements not equal to val is position
        return position

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [3, 2, 2, 3]
    val1 = 3
    length1 = solution.removeElement(nums1, val1)
    print(length1)  # Output: 2
    print(nums1[:length1])  # Output: [2, 2]

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    length2 = solution.removeElement(nums2, val2)
    print(length2)  # Output: 5
    print(nums2[:length2])  # Output: [0, 1, 3, 0, 4]

    nums3 = []
    val3 = 1
    length3 = solution.removeElement(nums3, val3)
    print(length3)  # Output: 0
    print(nums3)    # Output: []