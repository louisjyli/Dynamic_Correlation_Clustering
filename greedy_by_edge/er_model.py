__author__ = 'louisjyli'

import random

n = 1000
p = 0.8
t = 0

filename = 'er'+'_'+str(n)+'_'+str(p)+'.txt'
file = open(filename,'w+')

for i in range(n):
    for j in range(n):
        if i != j and random.uniform(0, 1) < p:
            file.write(str(i)+' '+str(j)+' '+str(t)+'\n')
            t += 1
        else:
            a =0
