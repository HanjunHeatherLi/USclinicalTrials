from pytrials.client import ClinicalTrials
import pandas as pd



ct = ClinicalTrials()

# Get 50 full studies related to Coronavirus and COVID in json format.
#ABP938_full= ct.get_full_studies(search_expr="aflibercept", max_studies=500)

# Get the NCTId, Condition and Brief title fields from 500 studies related to Coronavirus and Covid, in csv format.
fields = ct.get_study_fields(
    search_expr="SAMsung BIOepis + SB15",
    fields=["NCTId", "Condition","InterventionName","StartDate", "PrimaryCompletionDate", "CompletionDate", "EnrollmentCount", "Phase", "OrgFullName", "BriefTitle", "LocationCountry"],
    max_studies=500,
    fmt="csv",
)

# Get the count of studies related to aflibercept
# ClinicalTrials limits API queries to 500 records
# Count of studies may be useful to build loops when you want to retrieve more than 1000 records
#ct.get_study_count(search_expr="Coronavirus+COVID")

# Read the csv data in Pandas
raw_record = pd.DataFrame.from_records(fields[1:], columns=fields[0])
def clean_list(a_list):
    unique = set(a_list.split("|"))
    return list(unique)

raw_record['Location Country']=raw_record['LocationCountry'].apply(clean_list)
raw_record['Intervention Name']=raw_record['InterventionName'].apply(clean_list)
raw_record = raw_record.drop(columns=['LocationCountry','InterventionName'])
raw_record.to_csv('Samsung1.csv',index=False)

