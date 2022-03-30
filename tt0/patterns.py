ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[2;0H\u001B[2"
SMILE_COLOR = u"\u001B[31m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

import time

def smile_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(SMILE_COLOR, end="")
    print(sp + "  ___  ")
    print(sp + " /   \ ")
    print(sp + "| O o |")
    print(sp + " \ U / ")
    print(sp + "  ‾‾‾  ")
    print(sp + "       ")
    print(RESET_COLOR)

def smile():
  start = 0
  distance = 30 
  step = 1

  for position in range(start, distance, step):
      smile_print(position)  
      time.sleep(.1)

def diamond():
  sp1 = " " * 4
  sp2 = " " * 2
  print(sp1 + "↑" + sp1)
  print(sp2 + "↑   ↑" + sp2)
  print("←       →")
  print(sp2 + "↓   ↓" + sp2)
  print(sp1 + "↓" + sp1)