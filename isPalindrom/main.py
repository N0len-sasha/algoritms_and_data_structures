def ispalindrome(x):
    check = True
    y = list(str(x))
    for i in range(len(y)):
        check = check and (y[i] == y[len(y)-i-1])
    return check


print(ispalindrome(1233345321))
