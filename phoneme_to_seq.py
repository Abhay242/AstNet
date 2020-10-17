# These functions varies for dataset in use

import os
import scipy.io
import numpy as np

#prepare new dataset dct
def prep_dct():
    dct={}
    i=0
    f=open('dct.txt','r')
    lines=f.readlines()
    for line in lines:
        dct[(line[:-1])]=i
        i+=1
    return dct


# get new ema dataset phoneme label sequences (tab is used instead of space)
def to_sequence(file_pth,dct):
    seq=[]
    file= open(file_pth,'r')
    lines=file.readlines()
    for line in lines:
        line=line.split('\t')
        seq.append(dct.get(line[1][:-1]))
    file.close()
    return seq

#cliping the silence sequences
def clip_ema_silence(ema_path):
    pth_lst=ema_path.split('/')
    sub=pth_lst[2]
    F=int(pth_lst[-1].split('.')[0][-4:])
    #load ema data
    emamat=scipy.io.loadmat(ema_path)
    data=emamat['EmaData']
    #clipping
    startstoppth=(os.path.join("/".join(pth_lst[:4])))
    matfile=[f for f in os.listdir(startstoppth) if f.endswith('.mat')][0]
    ssmat=scipy.io.loadmat(os.path.join(startstoppth,matfile))
    BeginEnd=ssmat['BGEN']
    EBegin=np.int(BeginEnd[0,F-1]*100) # F: sent ID
    EEnd=np.int(BeginEnd[1,F-1]*100)
    data=np.transpose(data[:,EBegin:EEnd])# time X 18
    #normalization and artic deletion
    #data=np.delete(data, [4,5,6,7,10,11],1) # time X 12
    MeanOfData=np.mean(data,axis=0)
    data-=MeanOfData # Mean remov 
    #C=0.5*np.sqrt(np.mean(np.square(data),axis=0))
    #Ema=np.divide(data,C) # var normailized
    #print(Ema.shape,ema_path)
    return(data)
