import csv

def save_to_file(job_dic):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title","company","location","link"])
    for job in job_dic:
        writer.writerow(list(job.values()))
    return