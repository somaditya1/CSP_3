def seq_sum():
  num = int(input("Enter a number for your sequential sum: "))
  n = 0
  if num <= 0:
    print("This number has no sequence sum")
  else:
    for i in range(1, num + 1):
      n = n + i
    print("The sum of all numbers starting from 1 to", num, "is", n)