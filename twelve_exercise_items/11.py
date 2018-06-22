'''
Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''


def countBits(n):
    bn = bin(n).lstrip('0b')
    return sum(int(z) for z in bn)


print(countBits(1234))


def count(n):
    return format(n, 'b').count('1')


print(count(1234))
