"""
This module demonstrates the use of list comprehension
"""
# Nested for loops
words = [["Am", "ate", "ATOM", "apple"], ["bE", "boy", "ball", "bloom"]]
small_words = []
for letter_list in words:
    for word in letter_list:
        if len(word) < 3:
            small_words.append(word.lower())
# print (small_words)

# List comprehension
small_words = [word.lower() for letter_list in words for word in letter_list if len(word) < 3]

print(small_words)
