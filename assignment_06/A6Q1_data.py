# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6358: Software Tools for Business Analytics
#
# Sample script for Assignment 6, Question 1
#
# Name: Nicole Czubkowski 
# College of Business Administration
# University of Central Florida
#
# Date: 10/20/21
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



##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
os.chdir('C:\\Users\\19548\\Documents\\WEDNS-CLASS1\\assignment_06')
# Check that the change was successful.
os.getcwd()

####################
# List file names 
####################
path = 'C:\\Users\\19548\\Documents\\QMB6358F21\\QMB6358F21\\assignment_06\\housing_data'

House_data = os.listdir(path)

os.chdir('C:\\Users\\19548\\Documents\\QMB6358F21\\QMB6358F21\\assignment_06\\housing_data')

housing_single = []
housing_full = []
for i in House_data:
        #list file names
        print(i)
        
 ##################################################
# Load Data.
##################################################

# Loading one file at a time:
       
        #reading the files
        housing_single = pd.read_csv(i, index_col=None)
# Use a for loop to bind additional datasets to housing_full.
# Code goes here.

        #combining the files 
        housing_full = pd.concat([pd.read_csv(i) for i in House_data])
        housing_full.head()
    
##################################################
# Load Data.
##################################################
# Loading one file at a time:
# Use a for loop to bind additional datasets to housing_full.
# Code goes here.
# Calculate summary statistics for your data.
print(housing_full.describe())
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


