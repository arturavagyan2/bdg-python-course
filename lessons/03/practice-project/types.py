# B · Choose a type for a value · 8 minutes
#
# Investigate types after W2. Predict the starter's results before running. Explain why the two versions of thirty have different types, even if print displays similar characters.
#
# A locker label must preserve the text "042". A parcel count must calculate using the text "42". In the code area below the starter, store each fact under a readable name, keep the label as str, convert the count to int, and display each value and type. Also create a float from "4.9" and display its int conversion; explain why this is not rounding. Predict bool("0") and bool(0), then check them and explain the difference.
#
# **Check after modification:** label output still reads 042; count output reads 42 and its type is int; the truncated value from 4.9 is 4. Your explanation describes nonempty text rather than interpreting an English or numeric word. The initial prediction answers belong in your own notes.
#
# **Optional extension:** change the text passed to bool to empty text and then a single space. Predict both. No conditions or Boolean operators are needed.

written_count = "30"
number_count = 30
print(type(written_count))
print(type(number_count))
print(written_count + "2")
print(number_count + 2)
