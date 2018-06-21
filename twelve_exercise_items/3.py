# 写代码,要求实现以下功能给你一串字符串你要返回他的有重复的的字母个数
# 无视大小写

# test.assert_equals(duplicate_count("abcde"), 0)
# test.assert_equals(duplicate_count("abcdea"), 1)
# test.assert_equals(duplicate_count("indivisibility"), 1)


def duplicate_count(text):
    text_set = set(text.lower())
    count = 0
    for t in text_set:
        if text.count(t) != 1:
            count += 1
    return count


print(duplicate_count("indivisibility") == 1)


# def duplicate_count(text):
#     # Your code goes here
#     text = text.lower()
#     texts = set(text)
#     lists = []
#     for i in texts:
#         numbers = text.count(i)
#         if numbers != 1:
#             lists.append(numbers)
#     return len(lists)
