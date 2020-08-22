# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 05:28:42 2020

@author: PULPO
"""




'''
Dividir read per gen por gene lenght = rpk
sumo todos los rpk y divido por un millon = scaling factor
divido rpk de gen por el scaling factor = TPM del gen
 
'''






readPerGene = 'X:/bioinf/ovarios/intronLimAndGFF/rep_1_ovariosReadsPerGene.out.tab'
genLenght = 'X:/bioinf/index/genelenght.tab'
tpmFile = 'X:/bioinf/tpm3.tab'


fhRPG = open(readPerGene)
fhLenght = open(genLenght)
fo = open(tpmFile, 'a')

genes = dict()
rpkTot = 0
scaleFactor = 0
tot = 0.0 

for lines in fhRPG: #sumo los reads de cada gen
    line = lines.split()
    genes[line[0]] = int(line[2]) + int(line[3])
    
    
for lines in fhLenght: #saco el rpk sum(reads/lenght)
    line = lines.split()
    try:
        
        genes[line[0]] = float((genes.get(line[0])/(int(line[4]))))
    except: continue
    rpkTot += genes.get(line[0])
    


scaleFactor = rpkTot/1E6 


for key in genes:
    genes[key] = ((genes[key]/rpkTot))
    tot += genes[key]
    fo.write((str(key) + ' ' + str(genes[key]) + '\n'))  

fhRPG.close()
fhLenght.close()
fo.close()

#%%%

def get_week_day(argument):
    switcher = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    return switcher.get(argument, "Invalid day")
# Driver program

print (get_week_day(6))
print (get_week_day(8))
print (get_week_day(0))





def get_week_day(argument):
    def zero():
        return "Sunday"
    def one():
        return "Monday"
    def two():
        return "Tuesday"
    def three():
        return "Wednesday"
    def four():
        return "Thursday"
    def five():
        return "Friday"
    def six():
        return "Saturday"
    switcher = {
        0: zero(),
        1: one(),
        2: two(),
        3: three(),
        4: four(),
        5: five(),
        6: six()
    }
    return switcher.get(argument, "Invalid day")
# Driver program

print (get_week_day(6))
print (get_week_day(8))
print (get_week_day(0))









#%%%

import re

dataFile = '/media/pulpo/DB/bioinf/index/dm6.refGene.gtf'
outputFile = '/media/pulpo/DB/bioinf/index/refGeneNoCrom.gtf'


fh = open(dataFile)
fo = open(outputFile, 'a')

tot_Gen_Leng = 0


def converttostr(input_seq, separator):
   final_str = separator.join(input_seq)
   return final_str


def write_ref(line):
        separator = '	'
        fo.write(converttostr(line, separator)+'\n')



for lines in fh:
    line_List = lines.split()
    line_List[0] = '1'
    write_ref(line_List)
       
       
fh.close()
fo.close()









#%%%



import re

dataFile = 'X:/bioinf/index/dm6.refGene.gtf'
outputFile = 'X:/bioinf/index/maxTranscriptlenght.txt'


fh = open(dataFile)
fo = open(outputFile, 'a')

gene_Count = 0
tot_Gen_Leng = 0

gene_ID = re.findall('gene_id "([^"]+)', fh.readline())[0] #agarro la primera ID
transcript_ID = re.findall('transcript_id "([^"]+)', fh.readline())[0]

    
def reg_length (line):
    line_List = line.split()
    if (line_List[2] == 'exon'):
        min_temp = int(line_List[3])
        max_temp = int(line_List[4])
        return (max_temp-min_temp+1)
    return 0
    
def write_gen(gene_ID, transcript_ID, tot_Gen_Leng, gene_Count):
        fo.write((gene_ID + ' ' + transcript_ID + ' ' + str(tot_Gen_Leng) + '\n'))
        gene_ID = gene_ID_temp




for lines in fh:
    gene_ID_temp = re.findall('gene_id "([^"]+)', lines)[0]
    transcript_ID_temp = re.findall('transcript_id "([^"]+)', lines)[0]
    
    if (gene_ID_temp == gene_ID and transcript_ID_temp == transcript_ID):         
       tot_Gen_Leng += (reg_length(lines))
    
    else:
        gene_Count += 1
        write_gen(gene_ID, transcript_ID, tot_Gen_Leng, gene_Count)
        
        gene_ID = gene_ID_temp
        transcript_ID = transcript_ID_temp
        tot_Gen_Leng = (reg_length(lines))
        

write_gen(gene_ID, transcript_ID, tot_Gen_Leng, gene_Count)
fh.close()
fo.close()

#%%%



import re

#dataFile = 'X:/bioinf/index/dm6.refGene.gtf'
#outputFile = 'X:/bioinf/index/maxGenelenght.txt'
dataFile = '/media/pulpo/DB/bioinf/index/dm6.refGene.gtf'
outputFile = '/media/pulpo/DB/bioinf/index/maxGenelenght.txt'


fh = open(dataFile)
fo = open(outputFile, 'a')

gene_Count = 0
tot_Gen_Leng = 0

gene_ID = re.findall('gene_id "([^"]+)', fh.readline())[0] #agarro la primera ID

    
def reg_length (line):
    line_List = line.split()
    if (line_List[2] == 'exon'):
        min_temp = int(line_List[3])
        max_temp = int(line_List[4])
        return (max_temp-min_temp+1)
    return 0
    
def write_gen(gene_ID, tot_Gen_Leng, gene_Count):
        fo.write((gene_ID + ' ' + str(tot_Gen_Leng) + '\n'))
        gene_ID = gene_ID_temp




for lines in fh:
    gene_ID_temp = re.findall('gene_id "([^"]+)', lines)[0]
    
    if (gene_ID_temp == gene_ID):         
       tot_Gen_Leng += (reg_length(lines))
    
    else:
        gene_Count += 1
        write_gen(gene_ID, tot_Gen_Leng, gene_Count)
        
        gene_ID = gene_ID_temp
        tot_Gen_Leng = (reg_length(lines))
        

write_gen(gene_ID, tot_Gen_Leng, gene_Count)
fh.close()
fo.close()

