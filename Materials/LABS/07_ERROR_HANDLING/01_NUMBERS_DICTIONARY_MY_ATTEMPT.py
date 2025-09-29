def searching_nums(nbr :str,nums :dict):
	matched = nums.get(nbr)
	if matched:
		return True
	return False


numbers_dictionary = {} 

line = input()

while True:
	if line == 'Search':
		while (searched := input()) != 'Remove':
			if not numbers_dictionary:
				print('The dictionary is empty, there is is nothing to search for.')
				break

			try:
				if searching_nums(searched,numbers_dictionary):
					print(numbers_dictionary[searched])
			except KeyError:
				print("Number does not exist in dictionary")
		break

	number_as_string = line
	try:
		number = int(input())
	
	except ValueError:
		print('The variable number must be an integer')
		continue

	numbers_dictionary[number_as_string] = number 	

	line = input()


while (for_removal := input()) != 'End':
	try:
		del numbers_dictionary[for_removal]
	except KeyError:
		print('Number does not exist in dictionary')
	
print(numbers_dictionary)