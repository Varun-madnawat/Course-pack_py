#1. Write a Python program to demonstrate various ways of accessing the string- By using Indexing and slicing.
# s = "Swastik and Rtitk are good friends"
# print(s[::-1])
# print(s[:])
# print(s[-1])

#2. Write a Python program to print the string S with every character except vowels in S replaced by _.
#S = input("Enter a String/word: ")
#output = ""
#for i in range(len(S)):
    #if (S[i] == 'a' or S[i] == 'A' or S[i] == 'e' or S[i] == 'E' or S[i] == 'i' or S[i] == 'I' or S[i] == 'o' or S[i] =='O' or S[i] == 'u' or S[i] == 'U'):
        #output = output + S[i]
    #else:
        #output = output + '_'
#print(output)

#3. Write a Python program to split to extract a list of the words in a sentence. These words are then converted to uppercase letters within the list.
# l = 'This is a sentance'
# s = l.split()
# out = []
# for i in s:
#     out.append(i.upper())
# print(out)

#4. Write a Python program to check whether a given string is in Palindrome or not.
# S = input("Enter the string to check: ")
# if S == S[::-1]:
#     print("The given string is palindrome")
# else:
#     print('The given string is not palindrome')