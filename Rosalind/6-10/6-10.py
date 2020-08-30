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




# %%
# =============================================================================
#  ----- ejercicio 10 making a consensus -----
# =============================================================================

text_file_hamm = 'rosalind_cons.txt'
full_directory = os.path.join(rosalind_dir, text_file_hamm)

fh = (open(full_directory))



sequences = []  
temp_line = ''
for lines in fh:
    if (lines.startswith('>') is False):
        temp_line += lines.rstrip()
    if (temp_line != '' and lines.startswith('>')):
        sequences.append(temp_line)
        temp_line = ''
sequences.append(temp_line)
del temp_line

len_seq = len(sequences[0])

profile = {
    'A': [],
    'C': [],
    'G': [],
    'T': []
}


for n in range(len_seq): 
    profile['A'].append(0)
    profile['C'].append(0)
    profile['G'].append(0)
    profile['T'].append(0)



for seq in sequences:
    for i, nit_base in enumerate(seq):
        profile[nit_base][i] += 1



def return_nit_bas(bases):
    bases.sort(key = lambda x: x[0], reverse = True)
    print (bases)
    return bases[0][1]



consensus = ''
for i in range(len_seq):
    consensus += return_nit_bas([[profile['A'][i], 'A'], [profile['C'][i], 'C'],
    [profile['G'][i], 'G'], [profile['T'][i], 'T']])


print(consensus)

for k, v in profile.items():
    print(k, end = ': ')
    for i in range(len_seq):
        print(profile[k][i], end = ' ')
    print('\n')
    