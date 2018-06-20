# 写你的代码，代码输出结果
# accum("abcd")  # "A-Bb-Ccc-Dddd"
# accum("cwAt")  # "C-Ww-Aaa-Tttt"


# s:字符串
def accum(s):
    l = []
    for x, y in enumerate(s):
        z = y.upper() + y.lower() * x
        l.append(z)
    return '-'.join(l)


a = accum('abcd')
print(a)


# 原题解
# return '-'.join(y.upper() + y.lower()* x for x,y in enumerate(s))
