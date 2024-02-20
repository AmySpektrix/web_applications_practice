def alphabetize(name_string):
    list_of_names = name_string.split(",")
    sorted_list = sorted(list_of_names)
    sorted_string = ",".join(sorted_list)
    return sorted_string

def count_vowels_func(text):
    vowels = "aeiou"
    number_of_vowels = len([x for x in text if x in vowels])
    return number_of_vowels

def add_name_to_string(starting_string, names_to_add):
    starting_string_list = starting_string.split(", ")
    names_to_add_list = names_to_add.split(",")
    final_list = starting_string_list + names_to_add_list
    return ", ".join(sorted(final_list))
    