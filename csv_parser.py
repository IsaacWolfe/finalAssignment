from __future__ import print_function

def csv_parser(name):
	f = open(name, 'r')
	employees = { }
	for line in f:
		print(line)
		if line == "\n":
			print("Empty line. Skipping.")
			continue
		line = line.split(',')
#		if len(line) < 2:
#			if line[0].find("@") == -1:
#				print("Line is missing name. Skipping.")
#			else:
#				print("Line is missing email. Skipping.")
#			continue
#		elif line[0].find("@") != -1:
#			print("Invalid syntax: first element is not a name.")
#			continue
#		else:
			employees[line[0]] = line[1]
	f.close()
	return employees
