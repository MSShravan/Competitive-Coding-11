# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # If we need to remove all digits, return "0"
        if k >= len(num):
            return "0"
        
        # Use a stack to keep track of digits
        stack = []
        
        for digit in num:
            # While we can still remove digits (k > 0) and the current digit
            # is smaller than the top of the stack, remove the larger digit
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If we still have k digits to remove, remove from the end
        while k > 0:
            stack.pop()
            k -= 1
        
        # Convert stack to string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # If result is empty, return "0"
        return result if result else "0"