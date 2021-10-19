#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:07:49 2021

@author: somyakhare
"""
from bs4 import BeautifulSoup
import requests
import time


print("Put some skill you're unfamiliar with")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
page = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')

soup = BeautifulSoup(page.content, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

def find_jobs():
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a
            
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f: #w stands for writing in the file
                    f.write(f'''Company Name: {company_name.strip()} \n''')
                    f.write(f'''Required Skills: {skills.strip()} \n''')
                    f.write(f'''More Info: {more_info}''')
                
                print(f'File saved: {index}')

#Adding feaatures to the project
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)
    
    
    
    
