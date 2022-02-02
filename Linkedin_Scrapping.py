# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:35:51 2021

@author: B0219236
"""

import numpy as np
from selenium import webdriver
import pandas as pd
import numpy as np
import re
import time
from urllib.request import urlretrieve
from urllib.parse import quote


# from selenium.webdriver.common.keys import Keys

def get_num_of_employees(company_df,ip_colm,op_colm,prev_colm):
    for i in range(len(company_df)):
        company_name=company_df[ip_colm].iloc[i]
        # company_name_new=company_name.replace(" ","-")
        if type(company_df[prev_colm]) != None:
            company_url='https://www.linkedin.com/company/'+company_name+'/people/'
            driver.get(company_url)
            time.sleep(3)
    # temp_list=driver.find_elements_by_class_name('org-people-bar-graph-element__percentage-bar-info truncate full-width mt2 mb1 t-14 t-black--light t-normal')
  
            content = driver.find_elements_by_css_selector('strong')
            try:
                print('The number US Employees of company {} is {}'.format(company_name,content[0].text))
                temp_employee_num=content[0].text
                company_df[op_colm].iloc[i]=temp_employee_num
            except:
                company_df[op_colm].iloc[i]=None
        else:
            company_df[op_colm].iloc[i]=None
    
    return company_df

# The company list to be imported is entered here. Change path accordingly
company_df_full=pd.read_excel(r'C:\Users\b0219236\Downloads\Test Automation\List of Companies.xlsx') 
company_df=company_df_full
company_df['US Employees blank']=''
company_df['US Employees1']=''
company_df['US Employees2']=''
company_df['US Employees3']=''
company_df['US Employees4']=''
company_df['US Employees5']=''

search_url='https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
option = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'images':2, 'javascript':2}}
option.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(r"C:\Users\b0219236\Downloads\chromedriver.exe")
driver.get(search_url)
time.sleep(2)

email='japhijaadost@gmail.com' #ENTER YOUR EMAIL ID REGISTERED WITH LINKEDIN HERE
password='japhijaadost' #ENTER YOUR LINKEDIN PASSWORD

username_box=driver.find_element_by_name('session_key')
username_box.send_keys(email)
password_box=driver.find_element_by_name('session_password')
password_box.send_keys(password)
time.sleep(2)
login_button=driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
login_button.click()
time.sleep(2)
df_test=get_num_of_employees(company_df,'Company Name','US Employees1','US Employees blank')
df_test1=get_num_of_employees(df_test,'CompanyName','US Employees2','US Employees1')
df_test2=get_num_of_employees(df_test1,'Companyname','US Employees3','US Employees2')
df_test3=get_num_of_employees(df_test2,'Company-Name','US Employees4','US Employees3')
df_test4=get_num_of_employees(df_test3,'Company_Name','US Employees5','US Employees4')
df_test4.to_csv(r'C:\Users\b0219236\Downloads\Test Automation\Test_Output_All_entries.csv')




        


