

fileToRead = open("C:/pycode/scripts-for-work/rev_r1.txt","r+") #"D:/pyfiles/rev_r1.txt"
fileToWrite = open("C:/pycode/scripts-for-work/rev_r1_finished.txt","w+") #"D:/pyfiles/rev_r1_finished.txt"



content = [line.rstrip() for line in fileToRead]
contentrc = []

for row in content:
	print(row)
	

rowcounter = 0
	
for row in content:
	line = row.split("-")
	#print("line " + str(line))
	#print(line[1])
	partToList = list(line[0])
	#print(partToList)
	# basecounter = 0
	# for base in partToList:
		# if base == "A":
			# partToList[basecounter] = "T"
		# elif base == "T":
			# partToList[basecounter] = "A"
		# elif base == "G":
			# partToList[basecounter] = "C"
		# elif base == "C":
			# partToList[basecounter] = "G"
		# basecounter +=1
	partToList.reverse()
	partToList2 = "".join(partToList)
	#print(partToList2)
	contentrc.append(str(partToList2) + "-" + str(line[1]))
	rowcounter += 1

print("i5 reverse-complemented:")	
for row in contentrc:
	print(row)


	
#for row in content:
#	f.write(row + "\n")	


fileToWrite.write("i7 reversed:\n")	
for row in contentrc:
	fileToWrite.write(row + "\n")
	
fileToRead.close()
fileToWrite.close()



