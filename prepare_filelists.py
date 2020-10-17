#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:29:07 2020

@author: wtc3

creating filelists file for training and  validation
"""
import os
print(os.getcwd())
conversion=['Neutral','Fast'] ##neutral to fast
dataset='../RateExp' # Dataset path
inp=[];out=[];
for sub in os.listdir(dataset):
    path2ema_in=os.path.join(dataset,sub,conversion[0],'EmaClean')
    path2ema_out=os.path.join(dataset,sub,conversion[1],'EmaClean')
    inp+=[os.path.join(path2ema_in,x) for x in os.listdir(path2ema_in)]
    out+=[os.path.join(path2ema_out,x) for x in os.listdir(path2ema_out)]
    inp=sorted(inp);out=sorted(out)
with open('filelists/train.txt','w') as train, open('filelists/val.txt','w') as val, open('filelists/test.txt','w') as test:
    for n,o,i in zip(range(len(out)),out,inp):
        if (n)%10==0:
            test.write(o+'|'+i+'\n')
        elif (n)%10==1:
            val.write(o+'|'+i+'\n')
        else:
            train.write(o+'|'+i+'\n')

    