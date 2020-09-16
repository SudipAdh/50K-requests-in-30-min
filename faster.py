import concurrent.futures
import requests
import threading
import time
from bs4 import BeautifulSoup

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    # print(url)
    session = get_session()
    with session.get(url) as response:
       
        status_code = response.status_code
        
        
        # print(div)
        


def download_all_sites(sites):
    print(len(sites))
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)



# sites = [
#     "https://kathmandupost.com/national/2020/09/13/disappearance-commission-recommends-relief-package-for-conflict-victims-saying-the-pandemic-has-left-them-in-distress"
# ] * 1000
print("reading urls form txt files.....")
file = open('net_domains.txt', 'r')
lines = file.readlines()
stripped_lines = ["http://"+line.replace("\n", "") for line in lines]

sites = stripped_lines[0:13]

print("starting to request....")
start_time = time.time()
download_all_sites(sites)
duration = time.time() - start_time
print("requesting finished....")
print(f"Parsed {len(sites)} in {duration} seconds")