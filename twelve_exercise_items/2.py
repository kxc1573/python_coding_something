# 写代码, 输出结果

# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1

# get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b)+1))


print(get_sum(2, -9))
