# ## W2 · A dictionary gives each field a name
# A list of dictionaries keeps several records in order. Each record has the same field names. tickets[1] selects one record; ["seats"] reads a field within it. A string key and a list index do different jobs.
# 
# **Predict:** What type of value is tickets[1]?
# 
# **Try:** Add a third fictional booking and display its fields using the same loop.
tickets = [{"name": "Mia", "seats": 2},
           {"name": "Noah", "seats": 1}]
print(tickets[1]["name"])
tickets[1]["seats"] = 3
for ticket in tickets:
    print(ticket["name"], ticket["seats"])
