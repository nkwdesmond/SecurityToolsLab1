# python .\md5_lab1.py -i words5.txt -w hashesStudents\8.txt -o output.txt -sp pass6.txt -sh salted6.txt
# python .\md5_lab1.py -i words5.txt -w hashesStudents\8.txt -o output.txt
# python .\md5_lab1.py -i words5.txt -w hashesStudents\combined.txt -o output.txt -sp pass6.txt -sh salted6.txt
# python .\md5_lab1.py -i words5.txt -w salted6.txt -o output.txt

import hashlib
import argparse
import time
import string
import itertools
import random
import datetime

def hash(s):
    return hashlib.md5(s.encode()).hexdigest()

parser=argparse.ArgumentParser()
parser.add_argument("-i", action="store", dest="words5_file")
parser.add_argument("-w", action="store", dest="hashes_file")
parser.add_argument("-o", action="store", dest="output_file")
parser.add_argument("-sp", action="store", dest="saltedpw_file")
parser.add_argument("-sh", action="store", dest="saltedhashes_file")
args=parser.parse_args()

words5_file=open(args.words5_file,"r")
hashes_file=open(args.hashes_file,"r")
output_file=open(args.output_file,"w")
if(args.saltedpw_file):
    saltedpw_file=open(args.saltedpw_file,"w")
if(args.saltedhashes_file):
    saltedhashes_file=open(args.saltedhashes_file,"w")

words5=[]
words5hash=[]
hashes=[]

time_start=time.time()
print('\nStart time: ', datetime.datetime.now())

for line in words5_file:
    a=line.strip()
    words5.append(a)
    a = hash(a)
    words5hash.append(a)
    
count=0
for line in hashes_file:
    a=line.strip()
    hashes.append(a)
    count+=1
print('Number of hashes: ',count)

output=[0]*(len(hashes))
shashes=[0]*(len(hashes))
spw=[0]*(len(hashes))

completed=0

for i in range(len(words5hash)):
    for j in range(len(hashes)):
        if(words5hash[i]==hashes[j]):
            output[j]=words5[i]
            if(args.saltedpw_file):
                spw[j]=words5[i]+random.choice(string.ascii_lowercase)
            completed+=1

characters=string.ascii_lowercase + string.digits

print('\nStarting brute force')
for passwd in itertools.product(characters,repeat=5):
    if(completed==len(hashes)):
        break
    passwd=''.join(passwd)
    a = hash(passwd)
    for j in range(len(hashes)):
        if(output[j]==0 and a==hashes[j]):
            output[j]=passwd
            if(args.saltedpw_file):
                spw[j]=passwd+random.choice(string.ascii_lowercase)
            completed+=1
            break
print('Brute force completed\n')

for i in range(len(output)):
    output_file.write(str(output[i])+'\n')
    if(args.saltedpw_file):
        saltedpw_file.write(str(spw[i])+'\n')
    if(args.saltedhashes_file):
        shashes[i]=hash(str(spw[i]))
        saltedhashes_file.write(shashes[i]+'\n')
output_file.close()

for y in output, spw, shashes:
    print('Password:') if y==output else print('Salted password:') if y==spw else print("Hash of salted password:")
    print('Number of entries: ', len(y))
    for x in y:
        print(x)
    print('\n')

time_end = time.time()
print('Total time: ',time_end-time_start)