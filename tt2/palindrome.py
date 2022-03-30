import re


class Palindrome:
  def __init__(self, user_input):
    self.user_input = user_input
    self.letters = re.sub("[^a-zA-Z]+", "", self.user_input)
    self.length = len(self.letters)
  def __call__(self):
    range_text = int(self.length / 2)
    pali_true = 0
    for i in range(0, range_text):
      l1 = self.letters[i].lower()
      l2 = self.letters[len(self.letters) - i - 1].lower()
      if l1 == l2:
        pali_true += 1
      else:
        print("An error occurs at", self.letters[len(self.letters) - i - 1], "which is letter", len(self.letters) - i, "- This letter should be", self.letters[i])
    if pali_true == int(self.length / 2):
      print("This is a palindrome!")
    else:
      print("This is not a palindrome...")

def pali_tester():
  test_data1 = Palindrome(user_input='Racecar')
  test_data2 = Palindrome(user_input='A man, a plan, a canal - Panama?')
  test_data3 = Palindrome(user_input='Test text')
  test_data4 = Palindrome(user_input='Slash slash slash')
  print("Phrase 1: Racecar")
  test_data1()
  print("Phrase 2: A man, a plan, a canal - Panama?")
  test_data2()
  print("Phrase 3: Test text")
  test_data3()
  print("Phrase 4: Slash slash slash")
  test_data4()

