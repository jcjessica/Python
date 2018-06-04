# program that prints out a table with integers from decimal 0 to 255, it's hex number, and the character corresponding to the unicode with UTF-8 encoding

# using a loop
#for x in range(0, 256):
#	print('{0:d} {0:#04x} {0:c}'.format(x))

# using list comprehension
#ll = [('{0:d} {0:#04x} {0:c}'.format(x)) for x in range(0, 256)]
#print( "\n".join(ll) )
def numUpper(str):
	upper = 0
	nonwhite = 0

	for x in range(0, len(str)):
		if str[x].isupper():
			upper += 1
		if str[x].isspace():
			nonwhite += 1

	print('Upper {0}'.format(upper))
	print('Non-whitespace {0}'.format(nonwhite))
	return;

# call function with user input from command line (python3 syntax)
str = input("input the text: ")
numUpper(str)
