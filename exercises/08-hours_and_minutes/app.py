#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(seconds):
  
  hours = seconds/60/60
  minutes = seconds/60
  return int(hours),int(minutes)




#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))