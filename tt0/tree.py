def build_tree(height):
  i = 1
  while i <= height:
    print(" " * (height - i) + "X " * i)
    i = i + 1
  print(" " * (height - 3) + "|   |\n" + " " * (height - 3) + "L...⅃")
    

def treefunc():
  height = int(input("Enter height: "))
  build_tree(height)