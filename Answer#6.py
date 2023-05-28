#Write a Python program to sort a dictionary by key.
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
sorted_dict=sorted(color_dict.items())
print(dict(sorted_dict))