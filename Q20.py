# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {')': '(', '}': '{', ']': '['}

#         for char in s:
#             if char in mapping:
#                 top_element = stack.pop() if stack else '#'
#                 if mapping[char] != top_element:
#                     return False
#             else:
#                 stack.append(char)

#         return not stack


def is_valid(value:str):
    list = [] #[(
    dic = {")":"(","}":"{","]":"["}

    for char in value:
        if char in dic:
            if list:
                top_element = list.pop()
                print(top_element)
                if dic[char] != top_element:
                    return False
        else:
            list.append(char)
    return not list

print(is_valid('[({})]{}'))