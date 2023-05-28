#Write a Python program to count the number of characters (character frequency) in a string.
str= input("Enter a string:")
char={}
for i in str:
    if i in char:
        char[i]+=1
    else:
        char[i]=1
print("Count of the charceters of the entered string is",char)
        
