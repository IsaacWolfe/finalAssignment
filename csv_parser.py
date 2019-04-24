from __future__ import print_function

class CSV_Error:
	def __init__(self,l,d,e,n):
		self.line = l
		self.dependency = d
		self.error = e
		self.num = n

	def __repr__(self):
		if self.num == 0:
			return "Line: " + str(self.line) + " Error: " + self.error
		elif self.num == 1:
			return "Line: " + str(self.line) + " Error: " + self.error + "\n\tFirst Element: " + self.dependency
		elif self.num == 2:
			return "Line: " + str(self.line) + " Error: " + self.error + "\n\tName: " + self.dependency
		elif self.num == 3:
			return "Line: " + str(self.line) + " Error: " + self.error + "\n\tEmail: " + self.dependency

def csv_parser(name):
	f = open(name, 'r')
	g = open("errors.txt", 'w')
	employees = { }
	line_count = 1
	for line in f:
		if line == "\n":
			error0 = CSV_Error(line_count, "\n", "Empty line", 0)
			print(error0,"\n------\n", file=open("errors.txt",'a'))
			continue
		line = line.split(',')
		if len(line) < 2:
			if line[0].find("@") != -1:
				error1 = CSV_Error(line_count, line[0], "First element is not a name", 3)
				print(error1, "\n-----\n",file=open("errors.txt",'a'))
			else:
				error2 = CSV_Error(line_count, line[0], "Name does not have an associated email", 2)
				print(error2, "\n-----\n",file=open("errors.txt",'a'))
			continue
		elif len(line) > 2:
			error3 = CSV_Error(line_count, line[0], "Line contains too many variables", 1)
			print(error3, "\n-----\n",file=open("errors.txt", 'a'))
		elif line[0].find("@") != -1:
			error4 = CSV_Errors(line_count, line[0], "First element is not a name", 3)
			print(error4, "\n-----\n",file=open("errors.txt", 'a'))
			continue
		else:
			email = line[1][:-1]
			employees[line[0]] = email
		line_count+=1
	f.close()
	g.close()
	return employees
