# %%
from collections import Counter
import numpy as np 
import os

#rosalind_dir = '/media/pulpo/SD/python/Rosalind/Bioinf/'
rosalind_dir =  'X:/bioinf/scriptsPy/Rosalind/1-5'



# %%
# =============================================================================
#  ----- ejercicio 1 Contador de nucleotidos -----
# =============================================================================

text_file_dna = 'rosalind_dna.txt'
full_directory_1 = os.path.join(rosalind_dir, text_file_dna)

text_file_1 = (open(full_directory_1, "r")).read()
aminoacids = "ACGT"

letter_count = Counter(text_file_1.translate(str.maketrans('','')))
letter_count = {k: letter_count.get(k, 0) for k in aminoacids}
print("Frequency count of letter:\n", letter_count)




# %%
# =============================================================================
#  ----- ejercicio 2 transcribir DNA a RNA -----
# =============================================================================

text_file_rna = 'rosalind_rna.txt'
full_directory_2 = os.path.join(rosalind_dir, text_file_rna)

text_file_2 = (open(full_directory_2, "r")).read()

text_file_2 = text_file_2.replace('T', 'U')
print (text_file_2)




# %%
# =============================================================================
#  ----- ejercicio 3 strand complementario de DNA -----
# =============================================================================

text_file_trans = 'rosalind_revc.txt'
full_directory_3 = os.path.join(rosalind_dir, text_file_trans)

text_file_3 = (open(full_directory_3, "r")).read()

#-1 pq suma un \n al final
transcript = [None] * (len(text_file_3)-1) 

for x in range(len(text_file_3)-1):
    AA = text_file_3[(len(text_file_3)-2) -x] #-2 pq ultimo elemento es 917, pero lens devuelve 918
    if AA == 'A':
        transcript[x] = 'T'
    elif AA == 'C':
        transcript[x] = 'G'
    elif AA == 'G':
        transcript[x] = 'C'
    elif AA == 'T':
        transcript[x] = 'A'


transcripto_final = ''.join(transcript)       
print (text_file_3)
print (transcripto_final)




# %%
# =============================================================================
#  ----- ejercicio 4 crecimiento de conejos -----
# =============================================================================


meses = 6
crias = 2


def fib(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b

print (fib(meses, crias))



# %%
# =============================================================================
#  ----- Porcentaje de CG -----
# =============================================================================


s = (open('X:/bioinf/scriptsPy/Rosalind/1-5/rosalind_cg.txt', 'r')).read()

genes = s.split(">")[1:]
gc = []

for gene in genes:
    a = gene.count("C") + gene.count("G")
    b = gene.count("C") + gene.count("G") + gene.count("A") + gene.count("T")
    gc.append(float(a)*100/b)

print (genes[gc.index(max(gc))][:13])
print (max(gc))