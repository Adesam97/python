def most_frequent_char(string):
    char_count = {}
    max_count = 0
    max_char = ''

    # count the frequency of each character
    for c in string:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1

        # update the maximum count and character
        if char_count[c] > max_count or (char_count[c] == max_count and string.index(c) < string.index(max_char)):
            max_count = char_count[c] 
            max_char = c 
            
    #return max_count
    return max_char


def most_frequent_char_count(string):
    char_count = {}
    max_count = 0
    max_char = ''

    # count the frequency of each character
    for c in string:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1

        # update the maximum count and character
        if char_count[c] > max_count or (char_count[c] == max_count and string.index(c) < string.index(max_char)):
            max_count = char_count[c] 
            max_char = c 
            
    return max_count
print('Enter your sentence(s)')
my_string = str(input('>>'))
my_string = my_string.replace(" ", "") #to remove space count
most_common_char = most_frequent_char(my_string)
most_common_char_count = most_frequent_char_count(my_string)
print(most_common_char)
print(f"The most frequently occurring character is '{most_common_char}' with a count of {most_common_char_count}.") 
