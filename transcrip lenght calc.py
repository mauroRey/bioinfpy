# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 18:28:52 2020

@author: PULPO
"""


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

