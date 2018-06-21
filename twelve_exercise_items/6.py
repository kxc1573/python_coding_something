'''
给定：一个包含名称散列的数组

返回：格式为由逗号分隔的名称列表的字符串，除了最后两个名称之外，应该用连字符分隔。

例：
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
'''


def namelist(names):
    nl = [n['name'] for n in names]
    if len(nl) > 1:
        return '%s & %s' % (', '.join(nl[:-1]), nl[-1])
    else:
        return nl[0] if nl else ''


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([]))


# def namelist(names):
#     # your code here
#     if len(names) > 1:
#         return '{} & {}'.format(', '.join(i['name'] for i in names[:-1]), names[-1]['name'])

#     elif len(names) == 1:
#         return names[0]['name']
#     else:
#         return ''
