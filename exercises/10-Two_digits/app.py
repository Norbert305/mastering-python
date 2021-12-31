#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
  
  tens_digit = int(digit / 10)
  ones_digit = digit % 10
  
  return tens_digit, ones_digit
   


#Invoke the function with any interger as its argument.
print(two_digits(79))
