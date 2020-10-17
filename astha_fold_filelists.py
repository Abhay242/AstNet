#create 4 fold split as done in astha's paper [https://www.researchgate.net/publication/327388697_Relating_Articulatory_Motions_in_Different_Speaking_Rates]

import os
import numpy as np

Total_folds=4
#F=1 #(1 -> 4)
files_per_subject=460
Q=files_per_subject//Total_folds
valid_id=52
rates=['Slow','Neutral'] # out , in
d='N2S'
Dataset_dir='../RateExp' # dataset directory path
subjects=os.listdir(Dataset_dir)
print(subjects)
for F in range(1, Total_folds+1): 
    idx=[i for i in np.arange(files_per_subject)]
    test_ids=[i for i in np.arange((F-1)*Q,(F*Q))]## indicies used for splitting ##
    all_train=[x for x in idx if x not in test_ids]
    train_ids=all_train[valid_id:]##
    val_ids=all_train[0:valid_id]##

    for sub in subjects:
        inpath=os.path.join(Dataset_dir,sub,rates[0],'EmaClean')
        outpath=os.path.join(Dataset_dir,sub,rates[1],'EmaClean')	
        files_in=sorted(os.listdir(inpath))
        files_out=sorted(os.listdir(outpath))
        files=np.asarray([inpath+'/'+x+'|'+outpath+'/'+y+'\n' for x,y in zip(files_in,files_out)])
        print(files[0])
        folder='filelists/'+d+'/'+'fold'+str(F)+'/'	
        train_files=files[train_ids]
        val_files=files[val_ids]
        test_files=files[test_ids]
        with open(folder+'a_train_'+sub+'.txt','a') as train, open(folder+'a_val_'+sub+'.txt','a') as val, open(folder+'a_test_'+sub+'.txt','a') as test:
            _=[train.write(x) for x in train_files]
            _=[val.write(x) for x in val_files]
            _=[test.write(x) for x in test_files]






##################################################################
############		end 		##########################
##################################################################
