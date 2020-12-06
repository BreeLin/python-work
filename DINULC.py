f = open("g:/jiang lab/rotation/rotation/EcoliK12.fasta",'r')
lines = f.readlines()
str=''
for lines in lines:
	lines = lines.rstrip()
	if lines.startswith(">"):
		continue
	else:
		str += lines
		
		
percent = {}
seq = ''
for line in str:
	seq += line.strip()	
for i in range(len(seq)-1):
	dinulc = seq[i:i+2]
	if "N" in dinulc or "R" in dinulc or "M" in dinulc :
		continue
	elif dinulc in percent:
		percent[dinulc] += 1
	else:
		percent[dinulc] = 1

total_value = 0
for value in percent.values():
	total_value += value
for key in percent.keys():
	ratio = round(percent[key]/total_value*100,2)
	print('%s:%d,%.2f%%'%(key,percent[key],ratio))

