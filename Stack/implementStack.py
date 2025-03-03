'''
# Get Min from Stack

Given q queries, You task is to implement the following four functions for a stack:

push(x) – Insert an integer x onto the stack.
pop() – Remove the top element from the stack.
peek() - Return the top element from the stack. If the stack is empty, return -1.
getMin() – Retrieve the minimum element from the stack in O(1) time. If the stack is empty, return -1.
Each query can be one of the following:

1 x : Push x onto the stack.
2 : Pop the top element from the stack.
3: Return the top element from the stack. If the stack is empty, return -1.
4: Return the minimum element from the stack.

Examples:

Input: q = 7, queries = [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]
Output: [3, 2, 1]
Explanation: 
push(2): Stack is [2]
push(3): Stack is [2, 3]
peek(): Top element is 3
pop(): Removes 3, stack is [2]
getMin(): Minimum element is 2
push(1): Stack is [2, 1]
getMin(): Minimum element is 1

Input: q = 4, queries = [[1, 4], [1, 2], [4], [3]]
Output: [2, 2]
Explanation: 
push(4): Stack is [4]
push(2): Stack is [4, 2]
getMin(): Minimum element is 2
peek(): Top element is 2

Input: q = 5, queries = [[1, 10], [4], [1, 5], [4], [2]]
Output: [10, 5]
Explanation: 
push(10): Stack is [10]
getMin(): Minimum element is 10
push(5): Stack is [10, 5]
getMin(): Minimum element is 5
pop(): Removes 5, stack is [10]

'''

class Solution:
    def __init__(self):
        # code here
        self.st = []
        self.min_st = []
        
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        self.st.append(x)
        if not self.min_st or x <= self.min_st[-1]:
            self.min_st.append(x)

    # Remove the top element from the Stack
    def pop(self):
        # code here
        if self.st:
            if self.st[-1] == self.min_st[-1]:
                self.min_st.pop()
            self.st.pop()

    # Returns top element of Stack
    def peek(self):
        # code here
        if self.st:
            return self.st[-1]
        return -1

    # Finds minimum element of Stack
    def getMin(self):
        # code here
        if self.min_st:
            return self.min_st[-1]
        return -1



if __name__ == "__main__":
    # Example usage
    stObj = Solution()
    results = []
    
    q = int(input())
    # q = 7
    for _ in range(q):
        query = list(map(int, input().split()))
        # query = [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]

        if query[0] == 1:
            stObj.push(query[1])  # Push operation
        elif query[0] == 2:
            stObj.pop()  # Pop operation (no return value)
        elif query[0] == 3:
            results.append(str(stObj.peek()))  # Peek operation
        elif query[0] == 4:
            results.append(str(stObj.getMin()))  # GetMin operation

    print(" ".join(results))  
        
    
