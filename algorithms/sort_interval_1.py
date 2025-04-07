test1 = [(5,7), (15,29), (7,9), (1,5), (12,15), (29,34), (9,12)]

def sort_interval_1(intervals):
    return sorted(intervals, key=lambda x: x[0])

print(sort_interval_1(test1))

def sort_interval_2(intervals):
    