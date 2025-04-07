from math import inf
import re

Testcase1 = "Greedy selection ensures that once we pick a movie, we only consider movies that start after its end time."  
# (once, a) → (3)  

Testcase2 = "A greedy algorithm makes the optimal choice at each step. It does not reconsider previous choices."  
# (optimal, choices) → (6)  

Testcase3 = "The shortest distance between two words in a document is found using a linear scan approach."  
# (shortest, document) → (3)  

Testcase4 = "This problem can be solved efficiently using two pointers. However, if one of the words is missing, return -1."  
# (missing, solved) → (7)  

Testcase5 = "Finding the shortest distance between words is useful in natural language processing applications."  
# (not_present, words) → (-1)  # Word not found

def doc_shortest_dist(doc, word1, word2):
    if word1 == word2:
        return 0
    doc_clean = re.sub('^\w\s', '', doc)
    word_list = doc_clean.split()
    word_dict = {idx:word for idx, word in enumerate(word_list)}
    shortest = inf
    pos1 = -1
    pos2 = -1
    for idx, word in word_dict.items():
        if word == word1:
            pos1 = idx
        elif word == word2:
            pos2 = idx
        if pos1 != -1 and pos2 != -1 and abs(pos1 - pos2) < shortest:
            shortest = abs(pos1 - pos2)

    if shortest == inf:
        return -1
    else:
        return shortest
    
print(doc_shortest_dist(Testcase1, "once", "a"))  # Expected output: 3
print(doc_shortest_dist(Testcase2, "optimal", "reconsider"))  # Expected output: 6
print(doc_shortest_dist(Testcase3, "shortest", "document"))  # Expected output: 3
print(doc_shortest_dist(Testcase4, "missing,", "solved"))  # Expected output: 7
print(doc_shortest_dist(Testcase5, "not_present", "words"))  # Expected output: -1