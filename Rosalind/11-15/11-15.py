import os
#rosalind_dir = '/media/pulpo/SD/bioinf/Rosalind/Bioinf/'
rosalind_dir =  '/media/pulpo/DB/bioinf/scriptsPy/Rosalind/11-15/'

#%%
# =============================================================================
#  ----- ejercicio 11 crecimiento de conejos con mortalidad dinamica-----
# =============================================================================


max_months = 6
time_to_die = 3


def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in range(n-1):
      ages = [sum(ages[1:])] + ages[:-1]
      
  return sum(ages)


print(fib(max_months,time_to_die))  # Prints 4


#%%
 # =============================================================================
#  ----- ejercicio 12 nodes -----
# =============================================================================
import os
rosalind_dir= "X:/bioinf/scriptsPy/Rosalind/11-15/"
textfile = 'rosalind_grph.txt'
full_directory = os.path.join(rosalind_dir, textfile)

fh = (open(full_directory))

reads = dict()
tempid = ''
for lines in fh:
    if lines.startswith('>'):
        tempid = lines[1:14]
        reads[tempid] = ''
    else:
        reads[tempid] += lines.strip()

for k1, v1 in reads.items():
    for k2, v2 in reads.items():
        if (v1[-3:] == v2[:3]) and (k1 != k2):
            print (k1, k2)

''' USANDO REGEX ARMO DICT
with open(sys.argv[1], 'rU') as f:
  data = f.read().replace("\n","")

pattern = re.compile(r'>(?P<label>Rosalind_\d{4})\s*(?P<bases>[ACGT\s]+)')

dnastrings = collections.OrderedDict(pattern.findall(data))
'''


#%%
# =============================================================================
#  ----- ejercicio 13 offspring calculator -----
# =============================================================================

data = '19578 19088 16430 17219 18053 17990'

data = data.split()
    
def percen_dom_phen (couple):   
    couples = {
        1: 1*2,       # AA-AA
        2: 1*2,       # AA-Aa
        3: 1*2,       # AA-aa 
        4: (3/4)*2,   # Aa-Aa
        5: (1/2)*2,   # Aa-aa
        6: 0/6*2        # aa-aa 
    }
    print(couples[couple])
    return couples[couple]
    

prob = 0
for i, n in enumerate(data):
    prob += percen_dom_phen(float(i)+1)*int(n)

print(prob)





#%%
# =============================================================================
#  ----- ejercicio 14 common sequence  -----
# =============================================================================
import os
rosalind_dir= "/media/pulpo/DB/bioinf/scriptsPy/Rosalind/11-15/"
textfile = 'rosalind_lcsm.txt'
full_directory = os.path.join(rosalind_dir, textfile)
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


def longest_common_substring(s1, s2):
   m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
   longest, x_longest = 0, 0
   for x in range(1, 1 + len(s1)):
       for y in range(1, 1 + len(s2)):
           if s1[x - 1] == s2[y - 1]:
               m[x][y] = m[x - 1][y - 1] + 1
               if m[x][y] > longest:
                   longest = m[x][y]
                   x_longest = x
           else:
               m[x][y] = 0
   return s1[x_longest - longest: x_longest]


temp_seq = ''
temp_seq2 = ''
for i, seq in enumerate(sequences):
	if i <= 0: 
		temp_seq = seq
		continue
	temp_seq = longest_common_substring(temp_seq, seq)
    
    
''' USANDO BINARY SEARCH
def substr_in_all(arr, part):
  for dna in arr:
    if dna.find(part)==-1:
      return False
  return True

def common_substr(arr, l):
  first = arr[0]
  for i in range((len(first)-l+1)):

    part = first[i:i+l]
    if substr_in_all(arr, part):
      return part
  return ""

def longest_common_substr(arr):
  l = 0; r = len(arr[0])

  while l+1<r:
    mid = int((l+r) / 2)
    if common_substr(arr, mid)!="":
      l=mid
    else:
      r=mid

  return common_substr(arr, l)


for lines in fh:
    if (lines.startswith('>') is False):
        temp_line += lines.rstrip()
    if (temp_line != '' and lines.startswith('>')):
        sequences.append(temp_line)
        temp_line = ''
sequences.append(temp_line)
del temp_line

print(longest_common_substr(sequences))
'''    
    
#%%

# =============================================================================
#  ----- ejercicio 15 mendels second law  -----
# =============================================================================


k = 6                                                                       
N = 17                                                                          

from scipy.stats import binom
print(1 - binom.cdf(N - 1, 2 ** k, 0.25))
