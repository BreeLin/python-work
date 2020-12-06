f = open("g:/jiang lab/rotation/rotation/EcoliK12.fasta",'r')
KAT = open("KAT.txt","a") 

lines = f.readlines()
str=''
for each_line in lines:
	each_line = each_line.rstrip()
	if each_line.startswith(">"):
		continue
	else:
		str += each_line
	
		
k_mer = input("please design a k-mer: ")	

percent = {}
seq = ''
for line in str:
	seq += line.strip()	
for i in range(len(seq)-int(k_mer)-1):
	knulc = seq[i:i+int(k_mer)]
	if "N" in knulc or "R" in knulc or "M" in knulc :
		continue
	elif knulc in percent:
		percent[knulc] += 1
	else:
		percent[knulc] = 1


unique = 0
distinct = len(percent)
for key in percent.keys():
	if percent[key] == 1:
		print(key)
		unique += 1
print("when k-mer=",k_mer,", unique k-mer_number= ",unique,", distinct k-mer_number= ",distinct,file = KAT)

