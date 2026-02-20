import pandas as pd
import numpy as np
import requests

from openpyxl import Workbook

workbook = Workbook()
worksheet = workbook.active

technologies = ["Python", "Java", "JavaScript", "C++", "SQL"]

worksheet.title = "Job Postings"
worksheet.append(["Technology", "Number of Jobs"])

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"

response = requests.get(url)
data1 = response.json()

def get_number_of_jobs_T(technology):
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
    response = requests.get(url)
    data1 = response.json()
    
    count = 0
    for job in data1:
        if technology.lower() in job["Key Skills"].lower():
            count += 1
    return count

for tech in technologies:
    techno = tech
    count = get_number_of_jobs_T(tech)
    #print(techno, "-", count)
    data = techno + '-', str(count)
    
results = []

for tech in technologies:
    count = get_number_of_jobs_T(tech)
    results.append([tech, count])
    
df = pd.DataFrame(results, columns=["Technology", "Number of Job Postings"])

df.to_excel("job_postings.xlsx", index=False)

print("Job posting data successfully written to job_postings.xlsx")
