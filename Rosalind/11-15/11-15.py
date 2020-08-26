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

fh = (open(full_directory)).read()

len_seq = 0
consensus = ''

# creo el diccionario de bases, con un largo igual a las secuencias
profile = {
			'A': [],
			'C': [],
			'G': [],
			'T': []
}

for lines in fh:
	print(lines)
	if re.findall('^[^>]', lines): continue
	len_seq = len(lines)
	break


for n in range(len_seq-1): 
	profile['A'].append(0)
	profile['C'].append(0)
	profile['G'].append(0)
	profile['T'].append(0)

	
'''
for lines in fh:

	print(type(lines))

	if not lines.startswith('>'):
		for j, nit_bas in enumerate(lines):
			print(nit_bas)
			if nit_bas == '\n':break
			profile[nit_bas][j] += 1

		#print(int((i-1)/2))'''

def return_nit_bas(bases):
	bases.sort(key = lambda x: x[0], reverse = True)
	return bases[0][1]




for i in range(len_seq-1):
	consensus += return_nit_bas([[profile['A'][i], 'A'], [profile['C'][i], 'C'],
	[profile['G'][i], 'G'], [profile['T'][i], 'T']])


print(consensus)

for k, v in profile.items():
	print(k, end = ': ')
	for i in profile[k]:
		print(profile[k][i], end = ' ')
	print('\n')