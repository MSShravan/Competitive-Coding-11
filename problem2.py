# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                # Pop the top two operands
                b = stack.pop()
                a = stack.pop()
                
                # Perform the operation
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Division truncates toward zero
                    stack.append(int(a / b))
            else:
                # Convert string to integer and push to stack
                stack.append(int(token))
        
        # The final result is the only element left in the stack
        return stack[0]