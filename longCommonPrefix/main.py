def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for string in strs[1:]:
        tempPrefix = ""
        for i in range(min(len(prefix), len(string))):
            if prefix[i] == string[i]:
                tempPrefix += prefix[i]
            else:
                break
        prefix = tempPrefix
        if not prefix:
            break

    return prefix


s = ["flower", "flow", "flight"]
print(longestCommonPrefix(s))
