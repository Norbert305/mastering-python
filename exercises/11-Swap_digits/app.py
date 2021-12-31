#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(digit):
  
  tens_digit = int(digit // 10)
  ones_digit = digit % 10

  swapped_digit = str(ones_digit) + str(tens_digit)
  
  return swapped_digit
   
   
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(79))

