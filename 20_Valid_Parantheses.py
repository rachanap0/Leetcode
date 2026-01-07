# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.    

#TC: O(n)
#SC: O(n)
def isValid(s: str) -> bool:
    stack = []
    closeToOpen = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in closeToOpen:
            #check to make sure the stack is not empty and the top element is char
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            #could have more than one opening braces, so adding them to the stack.
            stack.append(char)
        return True
    
str = "([{}])"
print(isValid(str))