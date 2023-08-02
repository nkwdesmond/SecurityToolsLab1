import hashlib
import time
import string
import argparse
import itertools

hashTable = {}

def hash(s):
    return hashlib.md5(s.encode()).hexdigest()

def op(filename):
    return open(filename).read().split("\n")

def crack(hashh):
    if hashh in hashTable:
        return hashTable[hashh]
def save(d, outputFileName):
    l = []
    for k,v in d.items():
        if v is None:
            l.append(k+':NOT FOUND')
        else:
            l.append(k+':'+v)
    outputFile = open(outputFileName,"w")

    for i in range(len(l)):
        outputFile.write(str(l[i])+'\n')
    outputFile.close()
def bruteForceDict():
    print('brute forcing')
    # Define the set of characters to use for generating the strings
    characters = string.ascii_lowercase + string.digits

    # Specify the length of the strings
    string_length = 5

    # Generate all 5-letter strings
    all_strings = [''.join(p) for p in itertools.product(characters, repeat=string_length)]

    print('brute forcing done')
    return all_strings


parser=argparse.ArgumentParser()
parser.add_argument("-i", action="store", dest="words5_file")
parser.add_argument("-w", action="store", dest="hashes_file")
parser.add_argument("-o", action="store", dest="output_file")
parser.add_argument('-b', action='store_true')
args=parser.parse_args()

globalOne = time.time()

if args.b:
    d = bruteForceDict()
else:
    d = op(args.words5_file)

print('hashtable generating')
hashTable = {hash(p):p for p in d} #creates a dictionary where has is the key, passwd is the value
print('hashtable generating done')
h = op(args.hashes_file)
h.remove("")
print(h)

foundDict = {}

for hh in h:
    cracked = crack(hh)
    foundDict[hh] = cracked
    print(hh, cracked)
print(foundDict)
save(foundDict, args.output_file)
globalTwo = time.time()
print('total time: ',globalTwo-globalOne)