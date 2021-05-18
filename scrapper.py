import requests
from bs4 import BeautifulSoup



def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all('a')
    last_page = pages[-2].get_text(strip=True)
    return last_page

def extract_job(html):
    title=html.find("h2",{"class":"mb4"}).find("a")["title"]
    company, location=html.find("h3",{"class" : "mb4"}).find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]
    return {'title': title, 'company': company, 'location': location, "link": f"https://stackoverflow.com/jobs/{job_id}"}

def get_jobs(last_pages, url):
    jobs = []
    #for page in range(1,last_pages + 1):
    for page in range(1,1 + 1):
        print(f"Scrapping page {page}")
        result = requests.get(f"{url}&pg={page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for r in results:
            job = extract_job(r)
            jobs.append(job)
    return jobs


def get_lists(word):
  URL = f"https://stackoverflow.com/jobs?q={word}&pg=2"
  last_page = get_last_page(URL)
  job_dic = get_jobs(int(last_page), URL)
  return job_dic