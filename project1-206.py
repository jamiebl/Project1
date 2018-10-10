import os, pdb
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	#pdb.set_trace()
	in_file = open(file, "r")
	line = in_file.readline() #grab the first line
	list_of_dict = [] # an empty list to append everything together at the end

	while line:
		dic_file = {} #a dictionary for the file objects
		value = line.split(",")

		#establish values
		first_name = value[0]
		last_name = value[1]
		email = value[2]
		class_year = value[3]
		date_of_birh = value[4]

		#set up dictionary w/ keys and value_city_state
		dic_file["First"] = first_name
		dic_file["Last"] = last_name
		dic_file["Email"] = email
		dic_file["Class"] = class_year
		dic_file["DOB"] = date_of_birh

		list_of_dict.append(dic_file)
		line = in_file.readline()

	in_file.close()
	return list_of_dict

	pass

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	#First sort list based on key
	sort_list = sorted(data, key = lambda val: val[col])
	#empty_list = [val for val in sort_list if val["First"]]
	grab_first_item = sort_list[0] #grab first item in list
	grab_first_n = sort_list["First"]
	grab_first_l = sort_list["Last"]

	#print (grab_first_item)
	return (grab_first_n, grab_first_l)
	pass


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	list_tuple = [] # Create a empty list for tuples
	fresh_count = 0
	sopho_count = 0
	junior_count = 0
	senior_count = 0

	a = sorted(data, key = lambda col: col["Class"], reverse = True)
	#for word in data:
	#	if word["Class"] == "Freshman":
	#		fresh_count = fresh_count + 1
	#	elif: word["Class"] == "Sophomore":
	#		sopho_count = sopho_count + 1
	#	elif: word["Class"] == "Junior":
	#		junior_count = junior_count + 1
	#	else:
	#		senior_count + 1

	#f_count = data.count({"Class": "Freshman"})
	#so_count = data.count({"Class": "Sophomore"})
	#jun_count = data.count({"Class": "Junior"})
	#sen_count = data.count({"Class": "Senior"})

	senior_count = len([val for val in a if val["Class"] == 'Senior'])
	jun_count = len([val for val in a if val["Class"] == 'Junior'])
	so_count = len([val for val in a if val["Class"] == 'Sophomore'])
	f_count = len([val for val in a if val["Class"] == 'Freshman'])


	list_tuple.append(("Senior", senior_count))
	list_tuple.append(("Junior", jun_count))
	list_tuple.append(("Sophomore", so_count))
	list_tuple.append(("Freshman", f_count))

	sort_list = sorted(list_tuple, key = lambda col: col[1], reverse = True)
	return (sort_list)

	pass


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	#Want just the DOB keys
	#no_f = list(filter(lambda val: val["First"] in a))
	#split_dob = [val for val in a if val['DOB']]
	#print (no_f)

	pass

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written


	#for val in a:
	#	del a["Class"]

	#for val in a:
	#	del a["DOB"]

	sort_list = sorted(a, key = lambda x: x[col])
	#for value in sort_list:

	f = open(fileName, "w")
	f.write(str(sort_list))
	f.close()
	#print (sort_list)



	pass

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

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
