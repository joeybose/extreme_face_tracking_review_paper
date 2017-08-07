import numpy as np
import pandas as pd
import pdb
from os import listdir
from os.path import isfile, join
import re

data_dir = '/media/drive/ibug/300W/'
indoor = data_dir + '01_Indoor/'
outdoor = data_dir + '02_Outdoor/'
indoorDF = pd.DataFrame(columns=('imgPath','points'))
outdoorDF = pd.DataFrame(columns=('imgPath','points'))
globalDF = pd.DataFrame(columns=('imgPath','points'))
if __name__ == "__main__":
    indoor_files = [f for f in listdir(indoor) if isfile(join(indoor, f))]
    outdoor_files = [f for f in listdir(outdoor) if isfile(join(outdoor, f))]
    index_indoor = 0
    outdoor_index = 0
    index_global = 0
    for f in indoor_files:
        f_ = f.split('.')
        fname,ext = f_[0],f_[1]
        if ext == 'pts':
            pts_file = open(join(indoor,f),'r')
            pts = pts_file.readlines()[3:-1]
            fpath = indoor + f
            pts = [pt.strip('\n') for pt in pts]
            indoorDF.loc[index_indoor] = [fpath,pts]
            globalDF.loc[index_global] = [fpath,pts]
            index_indoor = index_indoor + 1
            index_global = index_global + 1
    for f in outdoor_files:
        f_ = f.split('.')
        fname,ext = f_[0],f_[1]
        if ext == 'pts':
            pts_file = open(join(outdoor,f),'r')
            pts = pts_file.readlines()[3:-1]
            pts = [pt.strip('\n') for pt in pts]
            fpath = outdoor + f
            outdoorDF.loc[outdoor_index] = [fpath,pts]
            globalDF.loc[index_global] = [fpath,pts]
            outdoor_index = outdoor_index + 1
            index_global = index_global + 1
indoorDF.to_csv('indoor_300w.csv',mode='a',header=True)
outdoorDF.to_csv('outdoor_300w.csv',mode='a',header=True)
globalDF.to_csv('global_300w.csv',mode='a',header=True)
