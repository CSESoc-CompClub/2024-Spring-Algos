from provided import *

# This is the first file containing material discussed directly in the lecture.
#
# Welcome to your training! Poco's set up some functions for you to fill out 
# and work on your fundamental knowledge before you progress onto the case! 

""" ------------------------------ Question 1 ------------------------------ """
# From 0 to a given number n (exclusive), return an array containing all the 
# numbers that are divisible by 3 or 5 but not numbers that are divisible by both.
#
# For example, if n = 18, then the returned list would be [3, 5, 6, 9, 10, 12].

def fizzbuzz(n: int) -> list[str]:   
    return None

""" ------------------------------ Question 2 ------------------------------ """
# Given an array, shift it by n amount and return the shifted array.
#
# For example, if you are given arr = [1,2,3,4] and k = 3, then the shifted list
# would look like [2,3,4,1].

def array_shift(arr: list[int], n: int) -> list[int]:
    return None

""" ------------------------------ Question 3 ------------------------------ """
# You've been given a stack of randomly arranged files and Poco needs you to 
# find where a specific file for him. 
#
# The files are represented in the form of an array, and you are required
# to return the index of the file, or -1 if the file could not be found.
#
# For example, files = [2, 3, 5, 1, 4]. If file_to_find = 5 then the function
# return 2, since arr[2] = 5. However, if file_to_find = 6, then the function 
# would return -1, since there is no value 6 in the files array.

def search(files: list[int], file_to_find: int) -> int:
    return None

""" ------------------------------ Question 4 ------------------------------ """
# As if you weren't already overworked, you've now been given a HUMONGOUS stack
# of files to look through. Judging by the size, looking through all of them 
# individually would have you stuck at the office for the next 3 decades. 
#
# You have to find the file for Poco, but you have to do it quickly! The 
# variables and problem is the same as the previous question, but now there 
# is a 3 second time limit imposed on your function.

def fast_search(files: list[int], file_to_find: int) -> int:
    return None

""" ------------------------------ Question 5 ------------------------------ """
# Poco's notes that the crime rate in Cee City fluctuates over the year, and he 
# wishes to see if there is a pattern to these fluctuations. Poco's given you 
# crime data for one year and he needs you to find and return the span of consecutive
# months where crime rates were collectively the highest. 
#
# You are given this data in the form of an array. For example, 
# [1, -1, 5, 1, -3, 0, 1, -1, -3, 1, 3, 4] represents crime being 1% higher 
# than the average in January, 1% lower than the average in February, 
# 5% higher than the average in March and so on.
# 
# The span of *consecutive* months where crime rates were collectively the highest 
# would be [1,3,4] since 1 + 3 + 4 = 8. This array is what you are required to return 
# in the below function.

def monthly_crime(crime_rates: list[int]) -> list[int]:
    return None