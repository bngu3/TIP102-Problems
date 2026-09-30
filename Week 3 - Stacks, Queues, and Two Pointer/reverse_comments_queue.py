from collections import deque

def reverse_comments_queue(comments):
    stack = [] 
    result = []
    for words in comments:
        stack.append(words)

    while stack:
        item = stack.pop()
        result.append(item)

    return result
    
        




print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))