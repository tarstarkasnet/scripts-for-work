#This program reads a column of indexes and reverse-complements them but keeps them in the same order

fileToRead = open("D:/pyfiles/split_pairs.txt","r+")
fileToWrite = open("D:/pyfiles/split_pairs_finished.txt","w+")

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
	#print(line[1])
	# partToList = list(line[1])
	# print(partToList)
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
	# partToList.reverse()
	# partToList2 = "".join(partToList)
	# print(partToList2)
	# contentrc.append(str(line[0]) + "-" + str(partToList2))
	# rowcounter += 1

	
print("first index (i7):")	
for i in index1:
	print(i)
	
print("second index (i5):")
for j in index2:
	print(j)