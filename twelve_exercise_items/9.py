'''
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'

expanded_form(70304) # Should return '70000 + 300 + 4'
'''


def expanded_form(n):
    l = []
    idx = 0
    while n > 0:
        if n % 10:
            l.append(str((n % 10) * (10 ** idx)))
        idx += 1
        n = int(n/10)
    l.reverse()
    return ' + '.join(l)


print(expanded_form(70304))


# def expanded_form(num):
#     nums = str(num)
#     x = []
#     for i in range(0,len(nums)):
#         if int(nums[i]) != 0:
#             s = str(int(nums[i]) * (10 ** (len(nums) - i - 1)))
#             x.append(s)
#     return ' + '.join(x)
