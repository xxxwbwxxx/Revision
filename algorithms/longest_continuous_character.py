test1 = 'aabbbbbaaccdd' # return 2,6
test2 = 'bassrrrrrrrea'
test3 = ''
test4 = 'abcdefghu'


def longest_continuous_character(text):
    if len(text) <= 0:
        return 0
    max_num = [0,0] # start, max
    current_text = ''
    current_num = 0
    start_pos = 0

    for i, char in enumerate(text):
        if current_text != char:
            current_text = char
            current_num = 1
            start_pos = i
        else:
            current_num += 1
            if current_num > max_num[1]:
                max_num = [start_pos, current_num]
            else:
                continue

    if max_num[1] == 0:
        return 0, 0
    
    return max_num[0], max_num[0] + max_num[1]-1

print(longest_continuous_character(test1))
print(longest_continuous_character(test2))
print(longest_continuous_character(test3))
print(longest_continuous_character(test4))

def longest_continuous_character1(text):
    if len(text) == 0:
        return (-1, -1)
    max_start, max_len = 0, 1
    current_start, current_len = 0, 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            current_len += 1
            if current_len > max_len:
                max_start, max_len = current_start, current_len
        else:
            current_start = i
            current_len = 1
    
    return max_start, max_start + max_len - 1

print(longest_continuous_character1(test1))