# ## W1 · A definition waits for a call
# def gives a reusable block a name. The indented body runs when the name is called with parentheses. Saving a definition alone does not run its body.
# 
# **Predict:** Which line prints first?
# 
# **Try:** Call show_ready a second time. The body should run twice.
def show_ready():
    print("Ready for the next booking")

print("Definition saved")
show_ready()
