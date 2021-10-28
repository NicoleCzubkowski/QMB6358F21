# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6358: Software Tools for Business Analytics
#
# Sample script for Assignment 6, Question 2
#
# Name: Nicole Czubkowski 
# College of Business Administration
# University of Central Florida
#
# Date:10/25/2021
#
#
##################################################
"""


##################################################
# Import Modules.
##################################################


import os # To set working directory
# import numpy as np # Not needed here but often useful
import pandas as pd # To read and inspect data
import statsmodels.formula.api as sm # Another way to estimate linear regression
import re
import itertools


##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
#os.getcwd()
# Change to a new directory.
#os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\QMB6358F21\\assignment_06')
# Check that the change was successful.
#os.getcwd()

# Find out the current directory.
os.getcwd()
# Change to a new directory.
os.chdir('C:\\Users\\19548\\Documents\\WEDNS-CLASS1\\assignment_06\\housing_tables')
# Check that the change was successful.
os.getcwd()


##rule to determine if a line is data and to pull the numbers out or not 
##Reading files
path = 'C:\\Users\\19548\\Documents\\WEDNS-CLASS1\\assignment_06\\housing_tables'
House_records = os.listdir(path)


# def read_file(is_data_row):
#     with open(is_data_row,'r') as f :
#         print(f.read())
        
# is_data_row = []
# for i in House_records:
#     if i.endswith(".tex"):
#         with open(i,'r') as read:
        
#            for line in read:
#                #get_numbers = is_data_row(line)
#                 if line[0].isdigit():
#                     is_data_row.append(line[0:])
        
#print(is_data_row)

#########
#Part A
#########
def is_data_row():
    with open ("housing_sales_week_1_day_1.tex", 'r') as f:
        for line in f :
            if line[0].isdigit():
                
                print(line.strip())
is_data_row()

##########
#Part B 
# #####

def get_obs_row():
    with open ("housing_sales_week_1_day_1.tex", 'r') as f:
        for line in itertools.islice(f,9,28):
            #if line[0].isdigit():
               data = [float(s) for s in re.findall('\d*\.?\d+',line)]
               print(data)
get_obs_row()   

#########
#Part C
##########         
##################################################
# Inspect the final dataset
##################################################


# Calculate summary statistics for your data.
housing_full.describe()
# Use this to check whether your data handling is working correctly.


##################################################
# Fit the Regression Model
##################################################

# After the full dataset is obtained:

# Fit the regression model.
reg_model_full_sm = sm.ols(formula = "house_price ~ income + in_cali + earthquake", 
                           data = housing_full).fit()



# Display a summary table of regression results.
print(reg_model_full_sm.summary())





##################################################
# End
##################################################




