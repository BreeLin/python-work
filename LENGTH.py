f = open("g:/jiang lab/rotation/rotation/EcoliO157.fasta",'r')
lines = f.readlines()
str = ''
for lines in lines:
	lines = lines.rstrip()
	if lines.startswith(">"):
		continue		
	else:
		str += lines
length = str.count("A") + str.count("T") + str.count("G") + str.count("C")

print(length) 

