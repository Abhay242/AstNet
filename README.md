# AstNet

**Code for paper :**  
    [Attention and Encoder-Decoder based models for transforming articulatory movements at different speaking rates.](https://arxiv.org/abs/2006.03107)


**Package reqiurements:**
 
    matplotlib==2.1.0
    tensorflow==1.15.2
    numpy==1.13.3
    inflect==0.2.5
    librosa==0.6.0
    scipy==1.0.0
    Unidecode==1.0.22
    pillow



**How to RUN :**

1.  Create filelists using *prepare_filelists.py* and set paths in *hparams.py*.
2.  Install above mentioned libraries.
3.  Run ' *python train.py --output_directory=outdir --log_directory=logdir* '
