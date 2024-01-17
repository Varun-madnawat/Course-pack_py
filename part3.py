#1. Write a program using a While loop that asks the user for a number, and prints a countdown from that number to zero.
# n = int(input())
# while n != 0:
#     print(n)
#     n = n - 1
# print(0)

#2. Write a program to print the given pattern:
#   *
#  * *
# * * *
#* * * *

# n=int(input("Enter the number of rows : "))
# row = 1
# while row <= n:
#     spaces = n - row
#     stars = row
#     print(" " * spaces, end="")
#     print("* " * stars)
#     row += 1


#3. Write a program to print the reverse of a given integer number.
# n = int(input())
# s = str(n)
# print(s[::-1])

#4. d.Write a program to get the Fibonacci series between 0 to 50.
# n = 50
# f = 0
# s = 1
# print("Fabonacci series: ")
# for i in range(10):
#     print(f,end = " ")
#     next = f + s
#     f = s
#     s = next

#5. Write a program to calculate the sum of series up to n terms. for example, if n=5 the series will become: 2 + 22+222+2222+2222.
# n = int(input())
# su_m = 0
# for i in range(1,n+1):
#     s = int(str(2) * i)
#     su_m =  su_m + s
# print(su_m)