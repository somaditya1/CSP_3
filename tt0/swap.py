def numberSwapper():
  age1 = input('Enter 1st Number: ')
  age2 = input('Enter 2nd Number: ')
  temp = age1
  age1 = age2
  age2 = temp
  print(age1, age2)

def lessNumSwap():
  age1 = input('Enter 1st Number: ')
  age2 = input('Enter 2nd Number: ')
  if age2 > age1:
    print(age1, age2)
  else:
    print(age2, age1)