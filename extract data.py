

import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv("Salary_Dataset_with_Extra_Features.csv")
print("data types: ",data.dtypes)
print("data head: ",data.head())
print("null: ",data.isnull().sum())
print("duplicated: ",data.duplicated())
print("columns names: ",data.columns)
print("Job Title: ",data["Job Title"])
data["experience"]=data["Salary"] //100000
data["age"]= 22 + data["experience"]
print(data.columns)

FED = data[data["Job Title"] == "Front End Developer"][["Job Title", "Salary"]].dropna().values.tolist()
SDE = data[data["Job Title"] == "Software Development Engineer"][["Job Title","Salary"]]
WD=data[data["Job Title"] == "Web Developer"][["Job Title","Salary"]]
TE=data[data["Job Title"] == "Test Engineer"][["Job Title","Salary"]]
fed_age=data[data["Job Title"] == "Front End Developer"][["Job Title" , "age"]].dropna().values.tolist()
sde_age=data[data["Job Title"] == "Software Development Engineer"][["Job Title","age"]].dropna().values.tolist()
wd_age= data[data["Job Title"] == "Web Developer"][["Job Title" , "age"]].dropna().values.tolist()
te_age=data[data["Job Title"] == "Test Engineer"][["Job Title" , "age"]].dropna().values.tolist()
job_saleries = {"Front End Developer": [500000, 500000, 300000, 700000, 600000, 800000, 264000, 300000, 500000, 400000],
    "Software Development Engineer": [156000, 180000, 300000, 500000, 1200000, 1200000, 1700000, 996000, 624000, 960000],
    "Web Developer": [200000, 100000, 100000, 240000, 300000, 200000, 200000, 200000, 300000, 400000],
    "Test Engineer": [1104000, 200000, 200000, 200000, 200000, 400000, 200000, 300000, 300000, 400000]}

developer_age= {"Front End Developer":[27, 27,25,29,28,30,24,25,27,26],
                "Software Development Engineer": [23,23,25,27,34,34,39,31,28,31],
                "Web Developer":[24,23,23,24,25,24,24,24,25,26],
                "Test Engineer": [33,24,2,24,24,26,24,25,25,26]}
fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

for job_title, salaries in job_saleries.items():
    axes[0].plot(salaries, label=job_title, linewidth=4)
axes[0].set_title("Salaries by Job Title")
axes[0].set_ylabel("Salary")
axes[0].legend()

for job_title, ages in developer_age.items():
    axes[1].plot(ages, label=job_title, linewidth=4)
axes[1].set_title("Ages by Job Title")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Age")
axes[1].legend()

plt.figure(figsize=(10,6))
for job_title in job_saleries.keys():
    plt.scatter(developer_age[job_title],job_saleries[job_title], label=job_title)
plt.title("Salaries vs Age by Job Title")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)


age_counts = {job_title: len(ages) for job_title, ages in developer_age.items()}
colors = ['#4F6272', '#B7C3F3', '#DD7596', '#8EB897']
explode = (0, 0.1, 0, 0)  # Offset the second slice
plt.figure(figsize=(7, 7))
plt.pie(age_counts.values(), labels=age_counts.keys(), colors=colors, explode=explode, autopct='%1.1f%%')
plt.title('Age Distribution by Job Title')


total_salaries = {job_title: sum(salaries) for job_title, salaries in job_saleries.items()}
plt.figure(figsize=(10, 8))
plt.bar(total_salaries.keys(), total_salaries.values(), color=colors)
plt.xlabel('Job Title')
plt.ylabel('Total Salary')
plt.title('Total Salaries by Job Title')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


