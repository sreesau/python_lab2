#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.
import random
import array
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lower_char= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
symbols= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
Max_len=8
combined_char=digits+lower_char+upper_char+symbols
rand_digits=random.choice(digits)
rand_lower=random.choice(lower_char)
rand_upper=random.choice(upper_char)
rand_symbols=random.choice(symbols)
temp_pass=rand_digits+rand_lower+rand_upper+rand_symbols
for i in range(Max_len-4):
      temp_pass=temp_pass+ random.choice(combined_char)
      pass_arr=array.array('u',temp_pass)
      random.shuffle(pass_arr)
password=""
for x in pass_arr:
      password+=x
print(password)
     

