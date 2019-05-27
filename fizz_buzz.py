#fizz_buzz.py: Solving the FizzBuzz question

#for loop generator from 1-100
for num in range(1,101):
  if num % 3 == 0 and num % 5 != 0:
    print("Fizz")
  elif num % 5 == 0 and num % 3 != 0:
    print("Buzz")
  elif num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  else:
    print(num)
