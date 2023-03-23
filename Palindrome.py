x = input("please insert a word ")
y = reversed(x)
if list(x)==list(y):
    print("is a palindrome")
else:
    print("is not a palindrome")