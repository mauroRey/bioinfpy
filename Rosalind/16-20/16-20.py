# =============================================================================
#  ----- ejercicio 16 protein mottifs  -----
# =============================================================================

import urllib.request                                   
import re
import os

rosalind_dir= "X:/bioinf/scriptsPy/Rosalind/16-20/"
textfile = 'rosalind_mprt.txt'
full_directory = os.path.join(rosalind_dir, textfile)
fh = (open(full_directory))

proteins = fh.read().strip().split()
fasta = urllib.request.urlopen("http://www.uniprot.org/uniprot/B5ZC00.fasta").read().decode("utf-8").split('\n')


'''
This means that position 1 always is N, position 2 and 4 are any amino acid except
 P, and position 3 is either A or T. Writing this as a pattern for searching using
 regular expression we get:

(N[^P][ST][^P])

However, regular expression does not automatically include overlapping patterns,
 so to include these as well we need to write the pattern like this:

(?=(N[^P][ST][^P]))
'''


for ID in proteins:
    fasta = urllib.request.urlopen("http://www.uniprot.org/uniprot/"+ID+".fasta").read().decode("utf-8").split('\n')

    templine=''
    for lines in fasta:
        if lines.startswith('>'):continue
        templine += lines.strip()
        
    print(ID)   
    for match in re.finditer(r'(?=(N[^P][ST][^P]))', templine):
        print(int(match.span()[0])+1, end = ' ')
    print('\n')
    

# ARREGLAR FORMATO, pero funciona