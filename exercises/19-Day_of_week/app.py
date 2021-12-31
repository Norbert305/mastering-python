#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(nday):
  
  dday=((3+nday)%7)    
  
  return dday


  



#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(1))