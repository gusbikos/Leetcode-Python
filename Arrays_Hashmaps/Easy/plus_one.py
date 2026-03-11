"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

class Solution:
    def plusOne(self, digits):
        my_list = []
        carry = 1
        print(f"Original digits: {digits}\n")

        # reversed gives the digits from last to first
        for digit in reversed(digits):
            print(f"Processing digit = {digit}, carry = {carry}")
            total = digit + carry
            print("total", total)
            if total == 10:
                my_list.append(0)
                carry = 1
            else:
                my_list.append(total)
                carry = 0
            print(f"  my_list = {my_list}, carry = {carry}")

        if carry == 1:
            my_list.append(1)
            print(f"Carry left, append 1: my_list = {my_list}")

        # Reverse to restore order
        my_list = my_list[::-1]
        print(f"Final result: {my_list}\n")
        return my_list

# Test
sol = Solution()
sol.plusOne([1, 2, 3])
sol.plusOne([9, 9, 9])

        

# Test examples
sol = Solution()
print("Example 1:")
sol.plusOne([1, 2, 3])  # Should print step by step

print("\nExample 2:")
sol.plusOne([9, 9, 9])  # Should print step by step


sol = Solution()
result = sol.plusOne([1,2,3])
print(result)

sol2 = Solution()
result_2 = sol2.plusOne([4,3,2,1])
print(result_2)

sol3 = Solution()
result_3 = sol3.plusOne([9])
print(result_3)

sol4 = Solution()
result_4 = sol4.plusOne([9,9])
print(result_4)

