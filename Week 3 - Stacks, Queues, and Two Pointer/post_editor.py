from collections import deque

def edit_post(post):
    queue = deque()
    result = ""
    for char in post:
        if char != " ":
            queue.append(char)
        else:
            word = ""
            for _ in range(len(queue)):
                queue.append(queue.popleft())

            while queue:
                word += queue.pop()

            result += word + " "

    while queue:
        result += queue.pop()
    return result

    



print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 
# tsooB ruoy tnemegagne htiw eseht spit
# kcehC tuo ym tsetal golv

