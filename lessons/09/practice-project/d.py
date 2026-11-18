# ## D · Make a report from book records · 10 min
# **Goal:** Transform related records into a name list and a lookup dictionary.
# 
# Use a list comprehension to collect titles with copies greater than zero. Then use a normal loop to create copies_by_title, mapping every title to its copy count. Print both results. Do not change books.
# 
# **Check:** Available titles are Python and Birds in that order. The lookup also contains Maps with 0. With no available books, the name list should be empty.
# 
# **Extra (optional):** Make a flat list of all titles with a loop, then compare it with an unfiltered comprehension.
books = [{"title": "Python", "copies": 2},
         {"title": "Maps", "copies": 0},
         {"title": "Birds", "copies": 1}]
# Build available_titles and copies_by_title.
