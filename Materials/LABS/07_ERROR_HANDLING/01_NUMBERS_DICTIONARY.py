numbers_dictionary = {}

while (line:= input())  != "Search": 
	number_as_string = line
	try:
		number_value = int(input()) 
		numbers_dictionary[number_as_string] = number_value 
	except ValueError:
		print('The variable number must be an integer')
		
searched = input() 

if not numbers_dictionary:
	exit('{}')

while searched != "Remove": 	
	if not numbers_dictionary:
		break

	match = numbers_dictionary.get(searched)
	
	try:
		if match:
			print(numbers_dictionary[searched]) 
	except KeyError:
		print('The number is not found in the dictionary')
	searched = input()
    

while (to_be_removed:=input()) != "End": 
	if not numbers_dictionary:
		break
	try: 
		del numbers_dictionary[to_be_removed]
	except:
		print('Number does not exist in dictionary')

print(numbers_dictionary)