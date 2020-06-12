import os 
import argparse 

#command line script is a .py file 



# Tell argparse to handle arguments
parser = argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy.")


#Tell argparse what arguments to expect
parser.add_argument("path", help="The filepath to  the file to be analyzed.")

#Get arguments from the user (list that has all arguments added)
args = parser.parse_args()



filename = args.path
f = open(filename, 'r')

# read data in file
data = f.readlines()
f.close()

#open a file for writing, removing mdout out of the analyze_mdout.py
base_filename = filename.split('.')
base_filename = base_filename[0]
output_filename = F'{base_filename}_Etot.txt'



f_write = open('Etot.txt', 'w+')

print(F'Writing output to {output_filename}')

f_write.write('Total Energy\n')


# loop thru lines in the file, create empty list
etot = []
for line in data:
    split_line = line.split()
 #get information from line

    if 'Etot' in line:
        etot.append(split_line[2])
        
etot = etot[:-2]
#up to but not including the last two items in the list 
       #print split line 2
        #get information from line
for energy in etot: 
      f_write.write(F"{energy}\n")
        
    


f_write.close()
