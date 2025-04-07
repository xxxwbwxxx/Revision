from typing import List, Tuple
test1 = [(1, 3), (2, 5), (4, 7), (6, 9), (8, 10)]  # Expected output: 3 (e.g., [(1,3), (4,7), (8,10)])
test2 = [(0, 5), (1, 2), (3, 4), (6, 7), (8, 9)]  # Expected output: 4 (e.g., [(1,2), (3,4), (6,7), (8,9)])
test3 = [(1, 10), (2, 3), (4, 5), (6, 7), (8, 9)]  # Expected output: 4 (e.g., [(2,3), (4,5), (6,7), (8,9)])
test4 = [(1, 2), (2, 3), (3, 4), (4, 5)]  # Expected output: 4 (watch all movies)
test5 = [(1, 10), (2, 9), (3, 8)]  # Expected output: 1 (only one can be watched)

def max_movies_watched(movies: List[Tuple[int, int]]) -> int:
    movies.sort(key=lambda x: x[1])
    
    last_end = 0
    ctr = 0

    for start, end in movies:
        if start >= last_end:
            ctr += 1
            last_end = end
    return ctr

print(max_movies_watched(test1))
print(max_movies_watched(test2))
print(max_movies_watched(test3))
print(max_movies_watched(test4))
print(max_movies_watched(test5))