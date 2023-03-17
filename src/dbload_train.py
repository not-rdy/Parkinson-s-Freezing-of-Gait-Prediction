import os
import pandas as pd
from tqdm import tqdm
from lib.DBManager import DBManager
from base.settings import connector, PATH_DATA_RAW

db = DBManager(connector)

filenames_train_defog = os.listdir(
    os.path.join(PATH_DATA_RAW, 'train', 'defog'))
filenames_train_notype = os.listdir(
    os.path.join(PATH_DATA_RAW, 'train', 'notype'))
filenames_train_tdcsfog = os.listdir(
    os.path.join(PATH_DATA_RAW, 'train', 'tdcsfog'))

print('Loading train defog ...')
for name in tqdm(
        filenames_train_defog,
        total=len(filenames_train_defog),
        colour='green'):
    file = pd.read_csv(
        os.path.join(PATH_DATA_RAW, 'train', 'defog', name))
    file['Patient_id'] = name.split('.')[0]
    db.write_df(
        df=file,
        table_name='train_defog',
        if_exist='append')

print('Loading train notype ...')
for name in tqdm(
        filenames_train_notype,
        total=len(filenames_train_notype),
        colour='green'):
    file = pd.read_csv(
        os.path.join(PATH_DATA_RAW, 'train', 'notype', name))
    file['Patient_id'] = name.split('.')[0]
    db.write_df(
        df=file,
        table_name='train_notype',
        if_exist='append')

print('Loading train tdcsfog ...')
for name in tqdm(
        filenames_train_tdcsfog,
        total=len(filenames_train_tdcsfog),
        colour='green'):
    file = pd.read_csv(
        os.path.join(PATH_DATA_RAW, 'train', 'tdcsfog', name))
    file['Patient_id'] = name.split('.')[0]
    db.write_df(
        df=file,
        table_name='train_tdcsfog',
        if_exist='append')
