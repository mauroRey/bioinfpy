import os
import re

#rosalind_dir = '/media/pulpo/SD/bioinf/Rosalind/Bioinf/'
rosalind_dir =  '/media/pulpo/DB/bioinf/scriptsPy/Rosalind/11-15/'


# %%
# =============================================================================
#  ----- ejercicio 6 Contador de mismatch -----
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
    
