f = open("g:/jiang lab/rotation/rotation/EcoliK12.fasta",'r')
KAT = open("KAT.txt","a") 

lines = f.readlines()
str=''
for lines in lines:
	lines = lines.rstrip()
	if lines.startswith(">"):
		continue
	else:
		str += lines
	
		
k_mer = input("please design a k-mer: ")	

percent = {}
seq = ''
for line in str:
	seq += line.strip()	
for i in range(len(seq)-int(k_mer)-1):
	dinulc = seq[i:i+int(k_mer)]
	if "N" in dinulc or "R" in dinulc or "M" in dinulc :
		continue
	elif dinulc in percent:
		percent[dinulc] += 1
	else:
		percent[dinulc] = 1


unique = 0
distinct = len(percent)
for key in percent.keys():
	if percent[key] == 1:
		print(key)
		unique += 1
print("when k-mer=",k_mer,", unique k-mer_number= ",unique,", distinct k-mer_number= ",distinct,file = KAT)

