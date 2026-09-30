
# not opimtal since we are using .sort (which takes o(nlogn) times)

def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result


def engagement_boost1(engagements):
    result = [0] * len(engagements)
    position = len(engagements) - 1

    left = 0
    right = len(engagements) - 1

    while left <= right:
        left_squared = engagements[left] * engagements[left]
        right_squared = engagements[right] * engagements[left]

        if left_squared > right_squared:
            result[position] = left_squared
            right -= 1
        else:
            result[position] = right_squared
            left -= 1
        position -= 1
    return result



print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))