#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  
  answer = (num // 100) + (num // 10) % 10 + num % 10

  return answer


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))

#number = int(input())
#try:

 # a = number // 100
#  b = number // (10 % 10)
#  c = number % 10
#  print(a + b + c)

#number = int(input())