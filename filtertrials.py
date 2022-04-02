import pandas as pd

raw_aflibercept = pd.read_csv ('ABP938_raw_record.csv')

Rege_Bayer = ['regeneron','Bayer']
Eylea_trials = raw_aflibercept.loc[raw_aflibercept['OrgFullName'].str.contains('|'.join(Rege_Bayer),case=False)]
#Other_trials = pd.concat([Eylea_trials, raw_aflibercept]).drop_duplicates(keep=False)
drug=['MYL-1701p', 'SB15','ABP 938', 'FYB203','CT-P42','SOK583A1']
pattern = '|'.join(drug)
biosim_trial = raw_aflibercept[raw_aflibercept['Intervention Name'].str.contains(pattern)]
biosim_trial.to_csv('ABP938_biosimilars.csv',index=False)