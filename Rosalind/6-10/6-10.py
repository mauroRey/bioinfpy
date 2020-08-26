# %%
import os

#rosalind_dir = '/media/pulpo/SD/python/Rosalind/Bioinf/'
rosalind_dir =  'X:/bioinf/scriptsPy/Rosalind/6-10/'


# %%
# =============================================================================
#  ----- ejercicio 6 Contador de mismatch -----
# =============================================================================

text_file_hamm = 'rosalind_hamm.txt'
full_directory_2 = os.path.join(rosalind_dir, text_file_hamm)

DNA = (open(full_directory_2, "r")).read().split('\n')

mismatch_cnt = 0


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
#  ----- ejercicio 8 RNa a proteina -----
# =============================================================================
import re

text_file_hamm = 'rosalind_prot.txt'
full_directory_2 = os.path.join(rosalind_dir, text_file_hamm)


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


RNA = (open(full_directory_2, "r")).read()
RNA_codons = re.findall('...', RNA)
proteina = ''


for codon in RNA_codons:
    if codones.get(codon) == 'Stop': break
    proteina += codones.get(codon)
    
    
    
# %%
# =============================================================================
#  ----- ejercicio 9 Finding mottifs in DNA -----
# =============================================================================    
text_file_subs = 'rosalind_subs.txt'
full_directory_2 = os.path.join(rosalind_dir, text_file_subs)

sequences = (open(full_directory_2, "r")).read().split('\n')


DNA = sequences[0]
mottifs = sequences[1]    

mottifs_len = len(mottifs)

pos = ''
for i, n in enumerate(DNA):
    if(DNA[i:i+mottifs_len] != mottifs): continue
    else: pos += str(i+1) + ' '
    
    
print (pos)



#%%
# =============================================================================
#  ----- ejercicio 4 crecimiento de conejos con mortalidad dinamica-----
# =============================================================================


max_months = 6
time_to_die = 3


def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in range(n-1):
      ages = [sum(ages[1:])] + ages[:-1]
      
  return sum(ages)


print(fib(max_months,time_to_die))  # Prints 4