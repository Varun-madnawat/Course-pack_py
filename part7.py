#1. a.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# def generate_square_dict(n):
#     square_dict = {}
#     for x in range(1, n + 1):
#         square_dict[x] = x * x
#     return square_dict
# my_dict = generate_square_dict(5)
# value_a = my_dict['a']
# print("Value associated with key 'a':", value_a)
# value_b = my_dict.get('b', 'Key not found')
# print("Value associated with key 'b' using get():", value_b)
# my_dict['c'] = 30
# print("Updated Dictionary:", my_dict)
# dictionary_length = len(my_dict)
# print("Length of the Dictionary:", dictionary_length)

#2. Create a dictionary and apply the following methods 1) Print the dictionary items 2) access items 3) use get() 4)change values 5) use len()
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print("Dictionary Items:", my_dict)
# value_a = my_dict['a']
# print("Value associated with key 'a':", value_a)
# value_b = my_dict.get('b', 'Key not found')
# print("Value associated with key 'b' using get():", value_b)
# my_dict['c'] = 30
# print("Updated Dictionary:", my_dict)
# dictionary_length = len(my_dict)
# print("Length of the Dictionary:", dictionary_length) 

#3. Write a Python script to sort (ascending and descending) a dictionary by value and find the smallest and largest value in the dictionary.
# def sort_dictionary_by_values(input_dict, reverse=False):
#     sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=reverse))
#     return sorted_dict
# my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1, 'e': 10}
# ascending_sorted_dict = sort_dictionary_by_values(my_dict)
# print("Sorted Dictionary (Ascending):", ascending_sorted_dict)
# descending_sorted_dict = sort_dictionary_by_values(my_dict, reverse=True)
# print("Sorted Dictionary (Descending):", descending_sorted_dict)
# smallest_value = min(my_dict.values())
# print("Smallest Value in the Dictionary:", smallest_value)
# largest_value = max(my_dict.values())
# print("Largest Value in the Dictionary:", largest_value)