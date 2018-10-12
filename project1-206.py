import os, pdb, copy
import filecmp
from collections import Counter
from dateutil.relativedelta import *
from datetime import date, datetime


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	#pdb.set_trace()
	"""This function takes in a file from your computer/files. It will return a

	list of dictionaries. The keys are from the first row in the data provided,
	with the values being the following rows. See comments on specific dets on how
	the function runs.
	"""
	#Open the file
	in_file = open(file, "r")

	#Note: First line == header. Use next() to start reading from the second line
	next(in_file)

	#Grabs the first line read, which is the second line in the file...
	line = in_file.readline()

	#Emp list to append the dictionaries
	list_of_dict = []


	while line:
		#Create dictionary, might also be able to do this outside the loop...
		dic_file = {}

		value = line.split(",")

		#Establish/Make values
		first_name = value[0]
		last_name = value[1]
		email = value[2]
		class_year = value[3]
		date_of_birh = value[4]

		#Set up dictionary w/ keys and values
		dic_file["First"] = first_name
		dic_file["Last"] = last_name
		dic_file["Email"] = email
		dic_file["Class"] = class_year
		dic_file["DOB"] = date_of_birh

		list_of_dict.append(dic_file)
		line = in_file.readline()

	#Don't forget to close file at the end when using a while loop.
	in_file.close()
	return list_of_dict

	pass

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	"""This function takes in a list of dictionaries and a key to sort on. This

	function will return the first item/student in that sorted list as a string.
	See comments for more specific dets.
	"""

	#Sort list based on key, but not a specific key
	sort_list = sorted(data, key = lambda val: val[col])

	#Grab the first item(index 0) in that sorted list
	grab_first_item = sort_list[0]

	#Grab the "first name" and "last name" key values from previous item
	grab_first_n = str(grab_first_item["First"])
	grab_first_l = str(grab_first_item["Last"])


	return grab_first_n + " " + grab_first_l
	pass


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	"""This function takes in a list of dictionaries and returns a list of tuples

	sorted by the number of students in that class from highest --> lowest.
	"""

	#Create an emp list for the tuples
	list_tuple = []

	#Estab values
	fresh_count = 0
	sopho_count = 0
	junior_count = 0
	senior_count = 0

	#Sort students by Class key from highest to low.
	list_stu = sorted(data, key = lambda col: col["Class"], reverse = True)

	#List comprehension instead of for loop, and then take the number of stu in each class
	#Probably could have shortened this into one longer loop, but oh well
	senior_count = len([val for val in list_stu if val["Class"] == 'Senior'])
	jun_count = len([val for val in list_stu if val["Class"] == 'Junior'])
	soph_count = len([val for val in list_stu if val["Class"] == 'Sophomore'])
	fresh_count = len([val for val in list_stu if val["Class"] == 'Freshman'])


	list_tuple.append(("Senior", senior_count))
	list_tuple.append(("Junior", jun_count))
	list_tuple.append(("Sophomore", soph_count))
	list_tuple.append(("Freshman", fresh_count))

	#Sort list of the four classes by the second column(value) from high-->low
	sort_list = sorted(list_tuple, key = lambda col: col[1], reverse = True)

	return (sort_list)

	pass


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	"""This function takes in a list of dictionaries and returns the month (1-12)

	that had the most births in the data. See comments for more spec details.
	"""

	#Made a deepycopy so OG data would not have been harmed/broken in any way
	dif = copy.deepcopy(a)

	#Want only the DOB keys-successful
	for value in dif:
		del value["Class"]
		del value["Email"]
		del value["First"]
		del value["Last"]

	#Now I have a list of the values from the DOB key
	#Probably could have dif too...eh
	data_dob = [val["DOB"] for val in dif]

	#Emp list for the month specfic data
	data_mo  = []

	#List of months/days/years
	#Split at the "/" in order to get three cats
	for str in data_dob:
		value = str.split('/')
		month = int(value[0])
		day  =  int(value[1])
		year = int(value[2])

		data_mo.append(month)

	#make emp dict in order to hold the key(num) and val(freq)
	number_counter = {}

	for number in data_mo:
		#if that number is currently in the dict, then do not increment
		#else increment before moving on to the next number
		if number in number_counter:
			number_counter[number] += 1
		else:
			number_counter[number] = 1

	#sort using dict get function/ for values with the highest freq at the top
	num = sorted(number_counter, key = number_counter.get, reverse = True)

	#Just return the first num in list
	top_1 = num[0]

	return top_1

	pass

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as first,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	"""This function takes in a list of dictionaries and returns nothing. However, a

	file is written in csv format.
	"""
	#Sort list by keys
	sort_list = sorted(a, key = lambda val : val[col])

	#Open file
	f = open(fileName, "w")

	#Run for loop where adding first name, last name, email to a file
	for value in sort_list:
		first = value["First"]
		last = value["Last"]
		email = value["Email"]
		f.write(first + "," + last + "," + email + "\n")
	f.close()




	pass

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
	"""This function takes in a list of dictionaries and returns the average sum_age

	of the students. The number returned is rounded to the nearest integer.
	See comments below for specific details on how to do/what happens in the func.
	"""

	#Create a deepcopy so the OG data is not messed up accidently
	dif = copy.deepcopy(a)
	#Run a for loop in order to delete the keys not needed
	for value in dif:
		del value["Class"]
		del value["Email"]
		del value["First"]
		del value["Last"]

	#Now I have a list of the values from  the DOB key ONLY
	data_dob = [val["DOB"] for val in dif]

	#Initialize an emp list for for a list of the years
	data_year  = []

	#List of months/days/years
	#Split at the "/" in order to get three categories
	for str in data_dob:
		value = str.split('/')
		month = int(value[0])
		day =   int(value[1])
		year = int(value[2])

		data_year.append(year)

	#Grab the current Year using datetime, 'date' will work, but is a diff format
	now = datetime.now()

	#Initialize an emp list for a list of current_age
	current_age = []

	#Run that for loop in order to get the current agesself.
	#Note: abs() is needed for the years that are greater than the current year
	for value in data_year:
		age = abs(now.year - value)
		current_age.append(age)

	#Find average: sum/amount of numbers in list = aver
	sum_age = sum(current_age)
	amount = len(current_age)

	return(int(sum_age/round(amount)))


	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
