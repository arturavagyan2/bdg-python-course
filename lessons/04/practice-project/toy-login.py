# # E1 · Toy credential comparison · 4 minutes
# 
# Build a tiny conditional exercise using W4's and. **This is not real authentication.** Hardcoded credentials are visible to anyone reading the script; do not use a real username/password or copy this pattern into an application.
# 
# For this toy only, print "Demo match" if both entered_name equals "demo_reader" and entered_code equals "paper-key". Otherwise print "Demo mismatch". The starter holds fictional entered values; keep them as assignments, so no secret input is involved. Decide the Boolean expression and add an if/else.
# 
# **Checks:**correct name+code→match; correct name+wrong code→mismatch; wrong name+correct code→mismatch; both wrong→mismatch. Change one fact at a time.
# 
# **Optional extension:** explain why or would violate this toy's stated rule. Do not add credential storage or actual login features.

entered_name = "demo_reader"
entered_code = "paper-key"
