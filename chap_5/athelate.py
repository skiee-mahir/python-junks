'''
The coach needs the fastest racer but he's an asshole. He saved data like an idiot with various formats.
So, I need to stick my ass to the chair for a bit longer and format down his mess.
It's really messy, did any one say messi? :D
'''
#takes tring input then converts it to a '.' seperator if the seperator is either ":" or '-'
def sanitize(time_string): 
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return mins + "." + secs 
#Function to raed file's line from the drive and split it on comma starts 
def get_data(filename):
	try:
		with open(filename) as file:
			# return file.readline().strip().split(",")
			file_data = file.readline().strip().split(",")
			return {'Name' : file_data.pop(0), 'DoB' : file_data.pop(0), 'Times': file_data}
	except IOError as IOerr:
		print("Where's ma file bae?" +  str(IOerr))
		return None

sarah = get_data("sarah2.txt")
#Let's use a dictionary object to hold data for sarah
# sarah_structured = dict() #a curly brace would have done the trick -_-
# sarah_structured ["Name"] = sarah.pop(0)
# sarah_structured ["DoB"] = sarah.pop(0)
# sarah_structured ["Times"] = sarah
print(sarah["Name"] +"'s fastest times are:" +str(sorted(sanitize(t) for t in sarah["Times"])[0:3]))
