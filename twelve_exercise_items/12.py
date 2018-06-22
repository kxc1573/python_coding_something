'''
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

#括号问题判断是否是有效空号
'''


def valid_parentheses(string):
    cnt = 0
    for s in string:
        if s == '(':
            cnt += 1
        if s == ')':
            cnt -= 1
    return True if cnt == 0 else False


print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))
