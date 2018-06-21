# 输入代码实现以下的内容
#
# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"


def likes(names):
    if len(names) < 2:
        name = names[0] if len(names) else 'no one'
        return '%s likes this' % name
    elif len(names) == 2:
        return '%s and %s like this' % (names[0], names[1])
    else:
        third = '%s others' % (len(names) - 2) if len(names) > 3 else names[2]
        return '%s, %s and %s like this' % (names[0], names[1], third)


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))


# def likes(names):
#     # your code here
#     if names:
#         if len(names) == 1:
#             return names[0] + ' likes this'
#         elif len(names) == 2:
#             return names[0] + ' and ' + names[1] + ' like this'
#         elif len(names) == 3:
#             return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
#         else:
#             return names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this'
#     else:
#         return 'no one likes this'
