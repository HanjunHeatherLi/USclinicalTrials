# US Regi
### Overview

US Regi can be used to pull key information from clinicaltrial.org. It is coded in Python, leveraging pytrials package which wrapper around the clinicaltrials.gov API. User interface is leveraging PyQt5 

### How to use
-Run main.py, and you will get a window to fill your request

![US Regi Request Window](https://github.com/HanjunHeatherLi/USclinicalTrials/blob/main/png/window.png)

-Input the keywords you are interested in

-Select your output from "NCTId", "Condition","InterventionName","LastKnownStatus", "StartDate", "PrimaryCompletionDate", "CompletionDate", "StudyFirstPostDate", "StudyFirstSubmitDate","MaximumAge", "MinimumAge","EnrollmentCount", "Phase", "OrgFullName", "BriefTitle", "LocationCountry", "PrimaryOutcomeDescription", "SecondaryOutcomeDescription"

-Click "GO!". Your search will be saved in a csv file in current folder

-With this csv file, you can generate tableau dashboard, here show one example

![Tableau Dashboard Example](https://github.com/HanjunHeatherLi/USclinicalTrials/blob/main/png/Dashboard_1.jpg)
