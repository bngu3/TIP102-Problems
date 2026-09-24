def navigate_research_station(station_layout, observations):
    letter_dict = {letter: i for i, letter in enumerate(station_layout)}
    distance = 0

    distance += letter_dict[observations[0]]

    for i in range(len(observations) - 1):
        curr_letter = observations[i]
        next_letter = observations[i + 1]

        distance += abs(letter_dict[next_letter] - letter_dict[curr_letter])

    return distance




station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))
