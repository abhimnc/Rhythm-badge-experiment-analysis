import csv

def main():

	hublog_filename = '/home/abhishek/Desktop/badgepi-dev-05_proximity.txt'
	with open(hublog_filename, 'r') as read_line:

			for line in read_line:
				
				if "data" in line:
					split_line = line.split(':')
					print(split_line)
					                          
																																																																																																																																						  

																																														  

if __name__ == "__main__":
	main()