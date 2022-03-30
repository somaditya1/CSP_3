class Consec_Nums:
  def __init__(self, num):
    self.num = num
  def __call__(self):
    if self.num <= 0:
      print("No sequencial sum for this number")
    else:
      n = 0
      for i in range (1, int(self.num) + 1):
        n = n + i
      print("The sum of all the numbers from 1 to", self.num, "is", n)

def consec_print():
  inp = int(input("Enter a number you want to find the sequential sum of: "))
  func = Consec_Nums(inp)
  func()