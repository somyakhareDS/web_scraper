#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:07:49 2021

@author: somyakhare
"""
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')

soup = BeautifulSoup(page.content, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
    

        print(f'''
              Company Name : {company_name}
              Required Skills : {skills}
              ''')
 
        print("  ")