import time
start_time = time.time()

sdc_file_name_path = 'SDC us_alliances_2000_2001.xls'
exe_file_name_path = 'execucomp 2000-2001.dta'

import numpy as np
import pandas as pd
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

sdc = pd.read_excel(sdc_file_name_path)
exe = pd.read_stata(exe_file_name_path)

l = []
cusips = []
for i in range(sdc.shape[0]):
    cusip = str(sdc['Partici-\npant\nParent\nCUSIP'][i]).split('\n')
    l.append(len(cusip))
    cusips.append(cusip)

for i in range(max(l)):
    sdc['partner ' + str(i + 1)] = np.nan

sdc['total\npartners'] = l

l = []
for cusip in tqdm(cusips, ncols=100, desc='SDC Partners'):
    match = -1
    c = 0
    for n in range(len(cusip)):
        for i in exe['CUSIP']:
            if i.find(cusip[n])+1 and match<n:
                c += 1
                match = n
    l.append(c)

for i in range(max(l)):
    sdc['partnerexec '+str(i+1)] = np.nan

sdc['total\npartners\nexec'] = l

for r, cusip in enumerate(tqdm(cusips, ncols=100, desc='EXE Partners')):
    match = -1
    c = 0
    for n in range(len(cusip)):
        sdc['partner ' + str(n + 1)][r] = cusip[n]
        for i in exe['CUSIP']:
            if i.find(cusip[n])+1 and match<n:
                sdc['partnerexec '+str(c+1)][r] = cusip[n]
                c += 1
                match = n

sdc.to_excel(sdc_file_name_path[:-5]+'_modified.xlsx')
print("--- %s seconds ---" % (time.time() - start_time))
