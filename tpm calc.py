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
tpmFile = 'X:/bioinf/tpm4.tab'


fhRPG = open(readPerGene)
fhLenght = open(genLenght)
fo = open(tpmFile, 'a')

genes = dict()
rpkTot = 0
scaleFactor = 0
tot = 0.0 
'''
RPG LENGHT RPKM TPM
#140.7344     320.7167
'''

totRC = 0
totrpk =0

for lines in fhRPG:
    if lines.startswith('N_'): continue
    line = lines.split()
    genes[line[0]] = [int(line[2])]
    totRC += int(line[2])
    
    
for lines in fhLenght: #rpkM = geneRC / ( geneLength/1000 * totRC/1,000,000 )
    line = lines.split()
    try: genes[line[0]].append(int(line[4]))
    except : continue

    if(genes.get(line[0]) == 'lola'):
        print(genes.get(line[0])[1])
        
    rpkm = float(genes.get(line[0])[0]) / (float(genes.get(line[0])[1]/1000) 
                                           * totRC/1E6)
    #rpk = (geneRC/(genelenght/1000))
    
    rpk = (genes.get(line[0])[0]) / ((genes.get(line[0])[1])/1000)
    
    genes[line[0]].append(rpkm)
    genes[line[0]].append(rpk)
    totrpk += rpk

    
scaleFactor = 1/totrpk * 1E6


fo.write('#Gene ID' + '\t' + 'reads per gene' + '\t' + 'lenght' + '\t' + 'RPK'
         +'\n' + 'TPM' +'\n') 
for gene_id in genes:
        
    tpm = scaleFactor * genes.get(gene_id)[3]
    genes[gene_id][3] = tpm
    fo.write((str(gene_id) + '\t' + str(genes[gene_id][0]) + '\n'))  

fhRPG.close()
fhLenght.close()
fo.close()
