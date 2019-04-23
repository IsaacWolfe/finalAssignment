from __future__ import print_function
import time
import sys

def csv_parser_file(name):
	f = open(name, 'r')
	employees = { }
	for line in f:
		line.split(',')
		if len(line) != 2:
			print("Invalid number of arguments.")
		elif line[1].find("@") != -1:
			print("Invalid syntax: first element is not a name.")
			continue
		else:
			person = [line[1], line[2]]
			email = line[3]
			employees[person] = email
	f.close()
	return employees

""" 
def getDay():



"""