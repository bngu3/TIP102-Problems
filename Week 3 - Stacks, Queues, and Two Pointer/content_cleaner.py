def clean_post(post):
    if post == "":
        return ""

    stack = []
    # poOst 
    for c in post:
        if (stack and c.lower() == stack[-1].lower() and c.isupper() != stack[-1].isupper()):
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)
        


print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 