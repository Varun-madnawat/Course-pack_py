#1. Write a Python program to create a tuple and perform the following methods: 1) check for the item in the tuple. 2)Access items 3) add items 4) len
# my_tuple = (1, 2, 3, 4, 5)
# item_to_check = 3
# if item_to_check in my_tuple:
#     print(f"{item_to_check} is present in the tuple.")
# else:
#     print(f"{item_to_check} is not present in the tuple.")
# first_item = my_tuple[0]
# last_item = my_tuple[-1]
# print(f"First item: {first_item}")
# print(f"Last item: {last_item}")
# new_items = (6, 7, 8)
# my_tuple += new_items
# tuple_length = len(my_tuple)
# print(f"Updated tuple: {my_tuple}")
# print(f"Length of the tuple: {tuple_length}")

#2. Write a Python program to find repeated items in a tuple.
# my_tuple = (1, 2, 3, 2, 4, 5, 6, 6, 7, 8, 9, 1)
# out = set(my_tuple)
# result = []
# for i in out:
#     n = my_tuple.count(i)
#     if n > 1:
#         result.append(i)
# print('Repeated number are: ', result)


#3. Write a Python program to create a Set and perform the following methods: 1) check for an item in Set. 2)Access items 3) Add items.
# my_set = {1, 2, 3, 4, 5}
# item_to_check = 3
# if item_to_check in my_set:
#     print(item_to_check,"is present in the set.")
# else:
#     print(item_to_check,"is not present in the set.")
# first_item = next(iter(my_set))
# print("First item:", first_item)
# new_items = {6, 7, 8}
# my_set.update(new_items)
# print("Updated set:", my_set)

#4. Write a Python Program that Displays which Letters are Present in Both the Strings.
# def find_common_letters(string1, string2):
#     common = set()
#     for letter in string1:
#         if letter in string2:
#             common.add(letter)
#     return common
    
# string1 = "hello"
# string2 = "world"
# result = find_common_letters(string1, string2)
# print("Common letters:", result)