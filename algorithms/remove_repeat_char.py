test1 = 'aaaabbcccd' # a4b2c3d
test2 = 'a' # a
test3 = '' # 

# def remove_repeated_char(text):
#     if not text:
#         return ""
#     result = []
#     curr_char = text[0]
#     ctr = 1

#     for i in range(1, len(text)):
#         if text[i] == text[i-1]:
#             ctr += 1
#         else:
#             result.append(curr_char)
#             if ctr > 1:
#                 result.append(str(ctr))
#             curr_char = text[i]
#             ctr = 1

#     result.append(curr_char)
#     if ctr > 1:
#         result.append(str(ctr))

#     return ''.join(result)

def remove_repeated_char(s):
    if not s:
        return []
    res = []
    ctr = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            ctr += 1
        elif s[i] != s[i-1]:
            if ctr > 1:
                res.append(s[i-1] + str(ctr))
            else:
                res.append(s[i-1])
            ctr = 1
    res.append(s[-1])
    if ctr > 1:
        res.append(str(ctr))
    return ''.join(res)

print(remove_repeated_char(test1))
print(remove_repeated_char(test2))
