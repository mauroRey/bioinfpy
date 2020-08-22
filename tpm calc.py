# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 05:28:42 2020

@author: PULPO
"""




'''

----------- T P M --------------------

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


for gene_id in genes:
    genes[gene_id] = ((genes[gene_id]/rpkTot))
    tot += genes[gene_id]
    fo.write((str(gene_id) + ' ' + str(genes[gene_id]) + '\n'))  

fhRPG.close()
fhLenght.close()
fo.close()


