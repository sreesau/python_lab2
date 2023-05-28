#Write a Python program to generate all sublists of a list.
def sub_lists (list):
	lists = [[]]    
	for i in range(0,len(list)+1):
		for j in range(i):
			lists.append(list[j:i])
	return lists


list = [1,2,3,4,5,6,7,8,9]
print(sub_lists(list))
