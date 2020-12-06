f = open("g:/jiang lab/rotation/rotation/EcoliK12.fasta",'r')
lines = f.readlines()
str=''
for each_line in lines:
	each_line = each_line.rstrip()
	if each_line.startswith(">"):
		continue
	else:
		str += each_line
		
		
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

