
################################################################################
#
# QMB 6358: Software Tools for Business Analytics
# Assignment 1, Question 2:
# Drafting Code for Functions
#
# Name: Nicole Czubkowski
# College of Business
# University of Central Florida
#
# Date: 8/27/2021
#
################################################################################
#
# This program defines the commands for a library of functions.
# Each function has a flaw.
# For each function, find three test cases that show examples
# of when the functions either fail or run correctly.
# Find at least one failure for each function.
#
#
################################################################################

# Load packages, if you need any.
# library(General Enviorment )


################################################################################
# Functions
################################################################################

#--------------------------------------------------------------------------------
# Function 1
#--------------------------------------------------------------------------------

is_it_3_or_4 <- function(num_in) {

  if (num_in >= 3 & num_in <= 4) {
    return(TRUE)
  } else {
    return(FALSE)
  }

}


#--------------------------------------------------------------------------------
# Function 2
#--------------------------------------------------------------------------------

multiples_of_ten <- function(num_1, num_2) {
  for (num in num_1:num_2) {
    if (num %% 10 == 0) {
      print(num)
    }
  }
}

#--------------------------------------------------------------------------------
# Function 3
#--------------------------------------------------------------------------------

count_even_numbers <- function(num_in) {
  count <- 0
  num <- 0
  while (num < num_in & count < 100) {
    num <- num + 1
    if (num %% 2 == 0) {
      count <- count + 1
    }
  }

  return(count) 
}

################################################################################
# Test cases
################################################################################

#--------------------------------------------------------------------------------
# Function 1
#--------------------------------------------------------------------------------

# Example:
is_it_3_or_4(3)

# Test cases with different inputs:

# Test case 1:
# Add a different function call in this line, like is_it_3_or_4(3), above.
#3 True works 

# Test case 2:
# Add a different function call in this line, like is_it_3_or_4(3), above.
#3.5 True does not work 

# Test case 3:
# Add a different function call in this line, like is_it_3_or_4(3), above.
#4 True works 


#--------------------------------------------------------------------------------
# Function 2
#--------------------------------------------------------------------------------

# Example:
multiples_of_ten(5, 32)

# Test cases with different inputs:

# Test case 1:
# Add a different function call in this line, like multiples_of_ten(5, 32), above.
#10,20,30 works 

# Test case 2:
# Add a different function call in this line, like multiples_of_ten(10, 10), above.
#10 does not work returns value num1 and num2 and it should not 

# Test case 3:
# Add a different function call in this line, like multiples_of_ten(10, 32), above.
#10, 20, 30 does not work becasue returns 10 and it should not include num1 


#--------------------------------------------------------------------------------
# Function 3
#--------------------------------------------------------------------------------

# Example:
count_even_numbers(11)

# Test cases with different inputs:

# Test case 1:
# Add a different function call in this line, count_even_numbers(11), above.
#5 works 

# Test case 2:
# Add a different function call in this line, count_even_numbers(20), above.
#10 works 

# Test case 3:
# Add a different function call in this line, count_even_numbers(220), above.
# 100 which is wrong it should be 110 but it only returns numbers 0-100 


################################################################################
# End 
################################################################################
