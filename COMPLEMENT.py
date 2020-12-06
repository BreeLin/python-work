f = open("g:/jiang lab/rotation/rotation/EcoliO157.fasta",'r')
Complement = open("COMPLEMENT.txt","w") 

lines = f.readlines()
str=''
for each_line in lines:
	each_line = each_line.rstrip()
	if each_line.startswith(">"):
		continue
	else:
		str += each_line

oldbase = ["G","T","C","A"]
newbase = ["C","A","G","T"]
for line in str:
	for old, new in zip(oldbase, newbase):
		if line == old: 
			line_new = line.replace(old, new)
			Complement.write(line_new)
		else:
			Complement.write(line)



