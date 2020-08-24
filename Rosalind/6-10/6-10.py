# %%
from collections import Counter
import os

#rosalind_dir = '/media/pulpo/SD/python/Rosalind/Bioinf/'
rosalind_dir =  'X:/bioinf/scriptsPy/Rosalind/6-10/'



# %%
# =============================================================================
#  ----- ejercicio 6 Contador de mismatch -----
# =============================================================================

text_file_hamm = 'rosalind_hamm.txt'
full_directory_2 = os.path.join(rosalind_dir, text_file_hamm)

fh = (open(full_directory_2, "r")).read()

mismatch_cnt = 0


DNA = fh.split('\n')
dna1 = DNA[0]
dna2 = DNA[1]

for i, n in enumerate(dna1):
    if n != dna2[i]: mismatch_cnt += 1


# %%
# =============================================================================
#  ----- ejercicio 7 primera ley mendel -----
# =============================================================================

#A son homocigota dominante, B heterocigota, C homocigota recesivo
a, b, c = 2,2,2

total = a+b+c


#Se forman 6 ecuaciones diferentes (AA*AA, AA*Aa, AA* aa, Aa*Aa, Aa*aa, aa*aa)
#simplifcando llegamos a esta ecuacion
percentage = ((a*((a-1) + 2*(b+c))) + (0.75*b*(b-1)) + (b*c)) / (total*(total-1))
#



# %%
# =============================================================================
#  ----- ejercicio 8 strand complementario de DNA -----
# =============================================================================
import re

codones = {
    'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
    'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
    'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
    'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
    'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
    'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
    'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
    'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
    'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
    'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
    'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
    'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
    'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
    'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
    'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
    'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'
}

RNA = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

RNA_codons = re.findall('...', RNA)
proteina = ''


for codon in RNA_codons:
    if codones.get(codon) == 'Stop': break
    proteina += codones.get(codon)