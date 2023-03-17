import os
import pandas as pd
from tqdm import tqdm
from lib.DBManager import DBManager
from base.settings import connector, PATH_DATA_RAW

db = DBManager(connector)

filenames_test_defog = os.listdir(
    os.path.join(PATH_DATA_RAW, 'test', 'defog'))
filenames_test_tdcsfog = os.listdir(
    os.path.join(PATH_DATA_RAW, 'test', 'tdcsfog'))

print('Loading test defog ...')
for name in tqdm(
        filenames_test_defog,
        total=len(filenames_test_defog),
        colour='green'):
    file = pd.read_csv(
        os.path.join(PATH_DATA_RAW, 'test', 'defog', name))
    file['Patient_id'] = name.split('.')[0]
    db.write_df(
        df=file,
        table_name='test_defog',
        if_exist='append')

print('Loading test tdcsfog ...')
for name in tqdm(
        filenames_test_tdcsfog,
        total=len(filenames_test_tdcsfog),
        colour='green'):
    file = pd.read_csv(
        os.path.join(PATH_DATA_RAW, 'test', 'tdcsfog', name))
    file['Patient_id'] = name.split('.')[0]
    db.write_df(
        df=file,
        table_name='test_tdcsfog',
        if_exist='append')
