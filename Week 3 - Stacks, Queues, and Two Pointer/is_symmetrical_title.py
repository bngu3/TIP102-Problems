"""
Understand: 
input: string
output: boolean

Match:
2 pointer, left and right


Planning:
have a left and right pointer, compare if the values are equal, if not return false,
else we move the pointers by 1 

"""


def is_symmetrical_title(title):
    left = 0
    s = title.replace(" ", "").lower()
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 