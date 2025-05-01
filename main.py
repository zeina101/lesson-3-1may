#PROGRAM TO ELIMINATE REPEATED LINES FROM A FILE

#creating the output file
outputFile = open('updatedfile.txt', 'w')

#reading the input file
inputFile = open('file.txt', "r")

#holds lines already seen
lines_seen_so_far = set()
print("Eliminating duplicate lines -- ")
#iterating each line in the file
for line in inputFile:

    # checking if line is unique
        if line not in lines_seen_so_far:
        
    #write unique lines in output file
        outputFile.write(line)
        
    #adds unique lines to linees_seen_so_far
        lines_seen_so_far.add(line)

    #closing the file
        inputFile.close()
        inputFile.close()
