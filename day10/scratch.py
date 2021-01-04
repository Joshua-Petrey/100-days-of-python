def times():
	result = 3 * 5
	return result

#Doc strings
def formatName(fname, lname):
	''' Take two strings: fname and lname. Outputs the the arguments as 
	a formatted string that is in title case '''
	formatted_fname = fname.title()
	formatted_lname = lname.title()
	return f"{formatted_fname} {formatted_lname}"


print(formatName("jOShuA", "PeTrEy"))
long = len(formatName("jghfg", "poprtter"))
print(long)

# functions can be  defined in other functions
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)