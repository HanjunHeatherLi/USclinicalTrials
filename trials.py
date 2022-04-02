from pytrials.client import ClinicalTrials
import pandas as pd


def huck_trial(search1, search2, selected):
    ct = ClinicalTrials()

# Get 50 full studies related to Coronavirus and COVID in json format.
#ABP938_full= ct.get_full_studies(search_expr="aflibercept", max_studies=500)

# Get the NCTId, Condition and Brief title fields from 500 studies related to Coronavirus and Covid, in csv format.
    fields1 = ct.get_study_fields(
        search_expr=search1,
        fields=selected,
        max_studies=500,
        fmt="csv",
    )
    fields2 = ct.get_study_fields(
        search_expr=search2,
        fields=selected,
        max_studies=500,
        fmt="csv",
    )

# Get the count of studies related to aflibercept
# ClinicalTrials limits API queries to 500 records
# Count of studies may be useful to build loops when you want to retrieve more than 1000 records
#ct.get_study_count(search_expr="Coronavirus+COVID")

# Read the csv data in Pandas
    record1 = pd.DataFrame.from_records(fields1[1:], columns=fields1[0])
    record2 = pd.DataFrame.from_records(fields2[1:], columns=fields2[0])
    raw_record = pd.concat([record1, record2], axis=0)
    def clean_list(a_list):
        unique = set(a_list.split("|"))
        empty = []
        if list(unique) != ['']:
            return list(unique)
        else:
            return empty

    if 'LocationCountry' in raw_record:
        raw_record['Location Country']=raw_record['LocationCountry'].apply(clean_list)
        raw_record['Country Num'] = raw_record['Location Country'].apply(lambda x: len(x))
        raw_record = raw_record.drop(columns=['LocationCountry'])
    if 'InterventionName' in raw_record:
        raw_record['Intervention Name']=raw_record['InterventionName'].apply(clean_list)
        raw_record = raw_record.drop(columns=['InterventionName'])
    raw_record.to_csv('customer.csv',index=False)

