
def mySqrt(x):
    if x < 0:
        x = x * -1
    s = 1
    prev = x
    while s * s <= x:
        prev = s
        s += 1
    return prev


print(mySqrt(4), 4**0.5)
print(mySqrt(8), 8**0.5)
print(mySqrt(7), 7**0.5)
print(mySqrt(6), 6**0.5)
