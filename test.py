import csv

def main():

	hublog_filename = '/home/abhishek/Desktop/openbadge-hub-py/local_file_hub_16_march_457pm.log'
	with open(hublog_filename, 'r') as read_line:

			for line in read_line:
				
				if "Found" in line:
					split_line = line.split(',')
					if(split_line[-1].split( )[0]=="'adv_payload':"):
						pass
					else:
						mac = split_line[1].split( )[-1]
						name = mac + "_file"
						
						project_id = split_line[-1].split( )[1].split('}')[0]
						voltage = split_line[-3].split(':')[1].strip()
						badge_id = split_line[-4].split(':')[1].strip()
						myData = [mac,badge_id,project_id,voltage]
						str_f = ' '.join(myData)
						f = open(name,'a')

						print(str_f)						
						f.write(str_f + '\n')
						f.close()                           
																																																																																																																																						  

																																														  

if __name__ == "__main__":
	main()