#Complete the function to return the tens digit of a given interger
def tens_digit(num):

  num = (num % 100) // 10

  return num


#Invoke the function with any interger.
print(tens_digit(1234))


#num = 1234

#thousands = num // 1000
#hundreds = (num % 1000) // 100
#tens = (num % 100) // 10
#units = (num % 10)

#print(thousands, hundreds, tens, units)
# expected output: 1 2 3 4