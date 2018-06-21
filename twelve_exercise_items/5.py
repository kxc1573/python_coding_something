# 你的任务是创建一个函数，它可以将任何非负整数作为参数，并以降序的数字返回它。
# 基本上，重新排列数字以创建尽可能高的数字。

# 例子：
# 输入：21445 输出：54421
# 输入：145263 输出：654321
# 输入：1254859723 输出：9875543221


def Descending_Order(num):
    return int(''.join(sorted(str(num), reverse=True)))


print(Descending_Order(21445))
print(Descending_Order(145263))

# def Descending_Order(num):
#     #Bust a move right here
#     nums = list(str(num))
#     nums.sort(reverse=True)
#     return int(''.join(nums))
