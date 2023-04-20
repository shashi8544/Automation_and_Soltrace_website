import os
import subprocess
import pandas as pd
import numpy as np

os.chdir(r'C:\Users\shuno\Desktop\Stirling')

excel_path = r'C:\Users\shuno\Desktop\sol_output_fin.xlsx'
fpath = r'C:\Users\shuno\Desktop\Stirling\input'
tmppath = r'C:\Users\shuno\Desktop\Stirling\input.tmp'
exepath = r'C:\Users\shuno\Desktop\Stirling\stirlingpro.exe'
respath = r'C:\Users\shuno\Desktop\Stirling\results'

heat_df = pd.read_excel(excel_path)
hotlst = list(heat_df['T_hot'])

# ITERATE OVER T_hot VALUES FROM EXCEL range: len(hotlst)
for i in range(len(hotlst)):
    print(i+1)

    #heater temp -> text[29] -> f'{T_HOT}\n'
    T_hot = hotlst[i]

    #in case of no output
    if T_hot == 0:
        text = """    ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
        NO OUTPUT AVAILABLE
        concentrated solar rays not falling on receiver.
        
        """
        tempf = open (r'C:\Users\shuno\Desktop\Stirling\Res\{}.txt'.format(i+1), 'w')
        tempf.writelines(text)
        tempf.close()
        continue

    # CHANGE INPUT FILE
    with open (fpath, "r") as f:
        text = f.readlines()
        text[29] = '{:.1f}\n'.format(T_hot)
        tempf = open (tmppath, 'w')
        tempf.writelines(text)
        tempf.close()
    f.close()
    os.remove(fpath)
    os.rename(tmppath, fpath)

    # EXECUTE SES SOFTWWARE
    subprocess.run(exepath)

    # SAVE RESULTS FILE IN RESULTS FOLDER
    with open (respath, "r") as f:
        text = f.readlines()
        idx = len(text) - 1 - text[::-1].index('    ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****\n')
        text_fin = text[idx:]
        tempf = open (r'C:\Users\shuno\Desktop\Stirling\Res\{}.txt'.format(i+1), 'w')
        tempf.writelines(text_fin)
        tempf.close()
    f.close()
    

