test1 = [["Rachel", 90], ["Monica", 80], ["Phoebe", 100], ["Rachel", 95], ["Monica", 90], ["Phoebe", 105]]
test2 = []
test3 = [["Rachel", 90]]

def max_average_grade(grades):
    if not grades:
        return -1
    result = {} # name: [sum, count]
    for name, grade in grades:
        if name in result:
            result[name][0] += grade
            result[name][1] += 1
        else:
            result[name] = [grade, 1]

    max_avg = 0
    for name in result:
        max_avg = max(max_avg, result[name][0] / result[name][1])
    return max_avg

print(max_average_grade(test1))
print(max_average_grade(test2))
print(max_average_grade(test3))
