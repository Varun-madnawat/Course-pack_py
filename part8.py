#1. Write a Python function that takes a number as a parameter and check the number is prime or not.
# def prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return 'Given number is not prime'
#     return 'Given number is prime'

# num = int(input("Enter a number: "))
# result = prime(num)
# print(result)

#2. Write a function unique which will return a list of unique elements is the list L in sorted order.
# def unique(l):
#     check = list(set(l))
#     return check

# l = [3, 1, 2, 2, 4, 3, 5, 4]
# output = unique(l)
# print(output)

#3. Write a Python function that prints out the first n rows of Pascal's triangle.
# def pascals_triangle(n):
#     triangle = []
#     for i in range(n):
#         current_row = [1] * (i + 1)
#         for j in range(1, i):
#             current_row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#         triangle.append(current_row)
#     return triangle
# num_rows = int(input("Enter the number of rows: "))
# result_triangle = pascals_triangle(num_rows)
# for row in result_triangle:
#     print(row)

