def init():
    global context
    context = {}
    context["authors"] = "Alex Blandin & William Webb"

def set(variable, value):
    context[variable] = value

def get(variable):
    return context[variable]
