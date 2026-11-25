def make_badge(name, **details):
    return {"name": name, "details": details}

print(make_badge("Mina", role="host", paid=False))
print(make_badge("Bo"))
