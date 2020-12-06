f = open("g:/jiang lab/rotation/rotation/EcoliO157.fasta",'r')
lines = f.readlines()
str=''
for each_line in lines:
	each_line = each_line.rstrip()
	if each_line.startswith(">"):
		continue
	else:
		str += each_line
		
length = str.count("A") + str.count("T") + str.count("G") + str.count("C")

print(length) 

