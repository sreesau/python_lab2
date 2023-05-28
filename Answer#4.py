#Write a python program to count repeated characters in a string.
string =input("Enter a string to find the repeated characters and its count: ") 
print("count of repeated characters in a given string: ") 
for i in range(0, len(string)):  
    count = 1
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1
            string = string[:j] + '0' + string[j+1:]; 
    
    if(count > 1 and string[i] != '0'):  
        print(string[i],count)