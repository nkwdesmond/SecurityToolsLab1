arr=[8,10,6,11,9,7,5,4,3,2,1,12,13,14,15,16,17,18,19,20]

import collections
print([item for item, count in collections.Counter(arr).items() if count > 1])

aaa=open('aaa.txt',"w")
for i in arr:
    for k in range(i):
        aaa.write('?a')
    aaa.write('\n')
