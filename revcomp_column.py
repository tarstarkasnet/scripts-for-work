#This program reads a column of indexes and reverse-complements them but keeps them in the same order

fileToRead = open("C:/pycode/scripts-for-work/revcomp_column.txt","r+")  #D:/pyfiles/revcomp_column.txt
fileToWrite = open("C:/pycode/scripts-for-work/revcomp_column_finished.txt","w+") #D:/pyfiles/revcomp_column_finished.txt

#strip any extra stuff and make a blank list
content = [line.rstrip() for line in fileToRead]
contentrc = []

#for the display
for row in content:
	print(row)
	

rowcounter = 0


for row in content:
	partToList = list(row)
	basecounter = 0
	for base in partToList:
		if base == "A":
			partToList[basecounter] = "T"
		elif base == "T":
			partToList[basecounter] = "A"
		elif base == "G":
			partToList[basecounter] = "C"
		elif base == "C":
			partToList[basecounter] = "G"
		basecounter +=1
	partToList.reverse()
	contentrc.append("".join(partToList))
	rowcounter += 1

#for display 
print("reverse-complemented:")	
for row in contentrc:
	print(row)

#write to the text file
fileToWrite.write("column reverse-complemented:\n")	
for row in contentrc:
	fileToWrite.write(row + "\n")
	
fileToRead.close()
fileToWrite.close()
