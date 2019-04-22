#This program reads a column of indexes and splits them into i7 and i5 columns in the same order

fileToRead = open("C:/pycode/scripts-for-work/split_pairs.txt","r+")
fileToWrite = open("C:/pycode/scripts-for-work/split_pairs_finished.txt","w+")

content = [line.rstrip() for line in fileToRead]
contentrc = []

for row in content:
	print(row)
	

rowcounter = 0
index1 = []
index2 = []
	
for row in content:
	line = row.split("-")
	print("line " + str(line))
	print("line[0] " + str(line[0]))
	print("line[1] " + str(line[1]))
	index1.append(line[0])
	index2.append(line[1])


	
print("first index (i7):")	
for i in index1:
	print(i)
	
print("second index (i5):")
for j in index2:
	print(j)
	

#Write to the text file	
fileToWrite.write("first index (i7):\n")	
for row in index1:
	fileToWrite.write(row + "\n")
	
fileToWrite.write("\n")

fileToWrite.write("second index (i5):\n")	
for row in index2:
	fileToWrite.write(row + "\n")
	
fileToRead.close()
fileToWrite.close()
