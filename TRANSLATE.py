import re
def translate(seq): 
    table = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R', 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    }
    start_sit = 'ATG'
    location = [m.start() for m in re.finditer(start_sit, seq)] 

    for site in location:
        protein=""
        for sit in range(site, len(seq), 3):
            protein += table[seq[sit:sit + 3]]
            if table[seq[sit:sit + 3]] == '_':
                print(protein[:-1])
                break
	      
f = open("g:/jiang lab/rotation/rotation/EcoliK12.fasta",'r')
#Translation = open("TRANSLATION.txt","w") 
lines = f.readlines()
str=''
for each_line in lines:
	each_line = each_line.rstrip()
	if each_line.startswith(">"):
		continue
	elif "N" in each_line or "R" in each_line or "M" in each_line:
		continue		
	else:
		str += each_line   
		          
translate(str)
