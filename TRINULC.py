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
for i in range(len(seq)-2):
	trinulc = seq[i:i+3]
	if "N" in trinulc or "R" in trinulc or "M" in trinulc :
		continue
	elif trinulc in percent:
		percent[trinulc] += 1
	else:
		percent[trinulc] = 1

total_value = 0
for value in percent.values():
	total_value += value
for key in percent.keys():
	ratio = round(percent[key]/total_value*100,2)	
	print('%s:%d,%.2f%%'%(key,percent[key],ratio))



