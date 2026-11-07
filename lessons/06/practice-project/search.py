# C · Find the first matching letter · 15 min
# Goal: Find the first match and handle no match.
# Read a word and one letter to find. Print its first position, counting from 1, or Not found. Use a loop, a position counter, a found flag and break. Letter case must match.
# Check cheese + e → Position: 3; cat + z → Not found.
# Extra: remove break in a copy. Explain why cheese now reports more than one position.

word = input("Word: ")
target = input("Letter: ")
position = 0
found = False
# Search the characters.
