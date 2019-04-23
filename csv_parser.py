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
	employees = { }
	errors = [ ]
	line_count = 1
	for line in f:
		if line == "\n":
			print("Error found. Skipping line.")
			errors.append(CSV_Error(line_count, "\n", "Empty line", 0))
			continue
		line = line.split(',')
		if len(line) < 2:
			if line[0].find("@") != -1:
				print("Error found. Skipping line.")
				errors.append(CSV_Error(line_count, line[0], "First element is not a name", 3))
			else:
				print("Error found. Skipping line.")
				errors.append(CSV_Error(line_count, line[0], "Name does not have an associated email", 2))
			continue
		elif len(line) > 2:
			print("Error found. Skipping line.")
			errors.append(CSV_Error(line_count, line[0], "Line contains too many variables", 1))
		elif line[0].find("@") != -1:
			print("Error found. Skipping line.")
			errors.append(CSV_Errors(line_count, line[0], "First element is not a name", 3))
			continue
		else:
			email = line[1][:-1]
			employees[line[0]] = email
	f.close()
	for i in errors:
		print(i)
	return employees
