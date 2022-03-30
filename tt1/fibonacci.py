def fibonacci():
  # creates a variable
  num = int(input("Enter the length of your Fibonacci sequence: "))
  #Prompts user to answer
  if num < 0:
    print("You cannot use a negative number")
  else:
    for i in range(num):
      print(recur_fibonacci(i))
      #Creates viable conditional

def recur_fibonacci(n):
  if n <= 1:  
     return n  
  else:  
     return(recur_fibonacci(n-2) + recur_fibonacci(n-1))