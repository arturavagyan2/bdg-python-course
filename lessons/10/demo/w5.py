# ## W5 · A loop finishes before its result returns
# A function can contain a familiar loop. Put return after the loop when the result needs every item. Returning inside the loop would stop the whole function on its first iteration.
# 
# **Predict:** Why does an empty list return 0?
# 
# **Try:** Change the limit from 3 to 4 and test a four-letter word.
def count_short_words(words):
    count = 0
    for word in words:
        if len(word) <= 3:
            count += 1
    return count

print(count_short_words(["map", "ticket", "bus"]))
print(count_short_words([]))
