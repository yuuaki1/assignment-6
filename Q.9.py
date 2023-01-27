class ParenthesesChecker:
    def __init__(self, string):
        self.string = string
        
    def is_valid(self):
        stack = []
        for char in self.string:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    return False
                current_char = stack.pop()
                if char == ")" and current_char != "(":
                    return False
                if char == "]" and current_char != "[":
                    return False
                if char == "}" and current_char != "{":
                    return False
        return not stack

# test the class
string1 = "()"
string2 = "()[]{}"
string3 = "[)"
string4 = "({[)]"
string5 = "{{{"

p1 = ParenthesesChecker(string1)
print(p1.is_valid()) #True

p2 = ParenthesesChecker(string2)
print(p2.is_valid()) #True

p3 = ParenthesesChecker(string3)
print(p3.is_valid()) #False

p4 = ParenthesesChecker(string4)
print(p4.is_valid()) #False

p5 = ParenthesesChecker(string5)
print(p5.is_valid()) #False
