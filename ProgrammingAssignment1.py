#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 05:05:58 2018

@author: t0
"""

import numpy as np
import time
import random
startTime=time.time()

def nu(n):
    n1=int(f'{random.randrange(10**(n-1),10**n):0n}')
    #generate random n-digt number
    a=list(map(int,str(n1)))
    #and put number in to list
    return a
def add(aa,bb):
    aa=np.int8(aa)
    bb=np.int8(bb)
    if 0==bb:
        return aa
    cor=aa^bb
    cand=aa&bb
    return add(cor,cand<<1)
def minus(a,b):
    return add(a,add(~b,1)) 
def cal(n):
    for d in range(1000):       
        a=nu(n)
        b=nu(n)
        s=""
        #a and b are the random numbers to subtract
        if a<b:
            c=a
            a=b
            b=c
            s="-"
        for i in range(n):
            a[n-i-1]=minus(a[n-i-1],b[n-i-1])
            #do subtract on each digt
            if a[n-i-1]<0:
                a[n-i-1]=a[n-i-1]+10
                a[n-i-2]=a[n-i-2]-1
        for i in range(n):
            s=s+str(a[i])
        s=int(s)
        #s is result of each full subtraction
cal(512)
#with cal(512), time spent is 15.9s on my computer
#cal(256) or other smaller n for cal(n) will reduce time
print('Time spent:{0}ms'.format(time.time()-startTime))
