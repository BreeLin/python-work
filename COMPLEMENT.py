f = open("g:/jiang lab/rotation/rotation/one_chromosome_human_genome.fasta",'r')
Complement = open("COMPLEMENT.txt","w") 

lines = f.readlines()
str=''
for lines in lines:
	lines.rstrip()
	if lines.startswith(">"):
		continue
	else:
		str += lines

oldbase = ["G","T","C","A"]
newbase = ["C","A","G","T"]
for line in str:
	for old, new in zip(oldbase, newbase):
		if line == old: 
			line_new = line.replace(old, new)
			Complement.write(line_new)
		else:
			continue

