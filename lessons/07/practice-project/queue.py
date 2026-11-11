# ## B · Repair the appointment queue · 16 min
# **Goal:** Distinguish a changed list from a method result.
# 
# The starter should add Ivo to the end but prints None. Run it and repair that line. Then insert Ema between Ada and Bo, remove Bo by name, serve the first person with pop(0), sort the remaining names and print both the served name and queue.
# 
# **Check:** Ada is served. The remaining queue is Ema then Ivo. Check after each change, not only at the end.
# 
# **Extra (optional):** In a copy start with Bo appearing twice. Investigate whether remove deletes one or both.

queue = ["Ada", "Bo"]
queue = queue.append("Ivo")
print(queue)
# Repair the assignment, then process the queue.
