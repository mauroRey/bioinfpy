# %%
from collections import Counter
import numpy as np 
import os

rosalind_dir = '/media/pulpo/SD/python/Rosalind/Bioinf/'




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


meses = 28
crias = 5

numero_conejos_mensual = np.zeros(shape=(1,meses))
numero_conejos_mensual[0,0]=1
numero_conejos_mensual[0,1]=1 


for n in range(meses-2):
    numero_conejos_mensual[0,n+2] = (numero_conejos_mensual[0,n+1] + \
                                     numero_conejos_mensual[0,n]*crias)
  
print (numero_conejos_mensual[0,meses-1])



# %%
# =============================================================================
#  ----- Porcentaje de CG -----
# =============================================================================


f = open('E:\python\Rosalind\Bioinf/rosalind_cg.txt', 'r')

max_gc_name, max_gc_content = '', 0

buf = f.readline().rstrip()
while buf:
    seq_name, seq = buf[1:], ''
    buf = f.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq = seq + buf
        buf = f.readline().rstrip()
    seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
    if seq_gc_content > max_gc_content:
        max_gc_name, max_gc_content = seq_name, seq_gc_content

print((max_gc_content * 100))