# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 18:32:00 2020

@author: PULPO
"""


#%%%


import time
start_time = time.time()

import re
dataFile = 'X:/bioinf/index/dm6.refGene.gtf'
outputFile = 'X:/bioinf/index/maxGenelenght.txt'
dataFile_Linux = '/media/pulpo/DB/bioinf/index/dm6.refGene.gtf'
outputFile_Linux = '/media/pulpo/DB/bioinf/index/maxGenelenght.txt'

try:
    fh = open(dataFile)
    fo = open(outputFile, 'a')
except:
    fh = open(dataFile_Linux)
    fo = open(outputFile_Linux, 'a')

del dataFile, outputFile, dataFile_Linux, outputFile_Linux


#################################
############ variables:  ########
#################################

genes = {}

gene_ID = re.findall('gene_id "([^"]+)', fh.readline())[0] #agarro la primera ID




#################################
############ functions:  ########
#################################




    
def exon_length (line):
    line_List = line.split()
    if (line_List[2] == 'exon'):
        min_temp = int(line_List[3])
        max_temp = int(line_List[4])
        return ([min_temp, max_temp])



#def check_superpos (gene_position, new_exon):
    
def merge_exons(gene_exon_list): 
          
        # Sorting based on the increasing order  
        # of the start intervals 
        gene_exon_list.sort(key = lambda x: x[0])  
          
        # array to hold the merged intervals 
        m = [] 
        s = -1E4
        max = -1E5
        for i in range(len(gene_exon_list)): 
            a = gene_exon_list[i] 
            if a[0] > max: 
                if i != 0: 
                    m.append([s,max]) 
                max = a[1] 
                s = a[0] 
            else: 
                if a[1] >= max: 
                    max = a[1] 
          
        #'max' value gives the last point of  
        # that particular interval 
        # 's' gives the starting point of that interval 
        # 'm' array contains the list of all merged intervals 
  
        if max != -100000 and [s, max] not in m: 
            m.append([s, max]) 
        lenght = 0
        for i in range(len(m)): 
            lenght += m[i][1] - m[i][0] + 1
        
        return lenght
        

def get_exons(gene_ID):
    for lines in fh:
        gene_ID_temp = re.findall('gene_id "([^"]+)', lines)[0]
        
        if (gene_ID_temp != gene_ID):
            gene_ID = gene_ID_temp
        else:
            if (gene_ID in genes):
                min_max_exon = exon_length(lines)
                if min_max_exon is not None:
                    genes[gene_ID] += [min_max_exon]
            else:
                genes[gene_ID] = [exon_length(lines)]




#################################
############    main:    ########
#################################
                
                
get_exons(gene_ID)

for ID in genes:
     max_lenght = merge_exons(genes.get(ID))
     fo.write((str(ID) + ' ' + str(max_lenght) + '\n')) 
     
     
fh.close()
fo.close()
print("--- %s seconds ---" % (time.time() - start_time))



#%%%

