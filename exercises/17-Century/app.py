#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.
import math
from math import ceil

def century(year):
  
  return (year - 1) // 100 + 1



#Invoke the function with any given year. 
print(century(2000))