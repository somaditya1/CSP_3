{% include navigation.html %}

# Data Structures Project Documentation
## Documentation of Individual Achievements
During this trimester, I learned a significant amount of concepts in CSP. I learned about the process of using and implemeting logins and authorization, CRUD, Databases, linking puthong to jinji2 in the backend, and connecting it all with Javascript and HTML on the front end. My greatest acheivment this trimester was establishing the Calendar linked to the Database and login with the help of Jakub and Akhil in particular. The user is forced to login with the admin account to be able to create, read, update, and delete events on the calendar. This assures that only credible people or the people who intended to edit the calender can. The python and jinja checks which month is selected, and updated the events on the specific days so that each month can have unique events, using the same div elements. I also contributed with creating a more aestheticly pleasing sleek calnder that took infromation from the database. This kept the calender to correspond with custom css style sheet for our website so that the theme’s were the same. Another aspect of our project that I was a key contributer was in communicating with the other teams to add important viable timezones to our project as requested by our sponser. I think that I utilized my time quite well this trimester and was able to accomplish a lot of our sponsor’s desires.

## What I learned:
adding tables within a database for organizing data
login and authorization/forcing account sign-in on certain pages
how to make a custom stylesheet for github pages
custom github pages theme
Personal acco mplishments Tangibles:
Calendar allowing for multiple events on one day
Calendar Popup JS
Custom GH Pages Style Sheet
simple blueprint for crossover team contributions

## Current Project Overview and Plans:

The website focuses on providing students with helpful and educational resources to further their education. This includes several classes, including CSP. Our plan is to keep adding on to the tutoring features and services present in “Backpack Pro”. Alongside this we also plan on incorporating some ideas or features requested by our Project Owner, such as platform-wide SCSS for platforms such as GitHub wikis and the Nighthawk Coder Society website. This would allow future students to access and read TPT and TT information without having to jump across multiple platforms, which would make the learning experience easier and more seamless We are also thinking about adding or creating a study calendar / organizer for CSP students, which would allow to plan our their week or studying so that they don’t procrastinate or forget to do anything. 


## Code Snippets
  
### Tech Talk 0 - Code

```   
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from menu import functions
import time

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Animation", functions.smile],
    ["Xmas Tree", functions.xmas_tree],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Swapping", functions.numberSwapper],
    ["Smaller # 1st", functions.lessNumSwap],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"



# def patterns_submenuc
# using patterns_sub_menu list:
# patterns_submenuc works similarly to menuc

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Swap Menu", submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Swap Submenu" + banner
    buildMenu(title, sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()

```

### Tech Talk 1

```
    
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Jakub",  
               "LastName": "Ponulak",  
               "DOB": "March 25",  
               "Residence": "San Diego",  
               "Email": "jakub.ponulak@gmail.com",  
               "Owns_Cars":["1997 BMW M3","2005 Subaru Impreza","1999 Nissan GTR Skyline","1997 Toyota Supra", "1990 Lamborghini Countach"]  
              })

InfoDb.append({  
               "FirstName": "John",  
               "LastName": "Cena",  
               "DOB": "April 23",  
               "Residence": "Hollywood",  
               "Email": "johncena@gmail.com",  
               "Owns_Cars":["2022 Invisi-Mobile"]  
              }) 

InfoDb.append({  
               "FirstName": "Akhil",  
               "LastName": "Nandhukamar",  
               "DOB": "April 1",  
               "Residence": "San Diego",  
               "Email": "akhiln@gmail.com",  
               "Owns_Cars":["2005 Ferarri FXX", "2005 Honda CRV"]  
              })  

InfoDb.append({  
               "FirstName": "Elon",  
               "LastName": "Musk",  
               "DOB": "June 28",  
               "Residence": "Los Angeles",  
               "Email": "elonmusk@gmail.com",  
               "Owns_Cars":["2022 Tesla Model X", "Tesla Cybertruck"]  
              })  


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def tester1():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling for invalid input
def fibonacci():
  num = int(input("Enter the length of your Fibonacci sequence: "))
  if num < 0:
    print("You cannot use a negative number")
  else:
    for i in range(num):
      print(recur_fibonacci(i))

def recur_fibonacci(n):
  if n <= 1:  
     return n  
  else:  
     return(recur_fibonacci(n-2) + recur_fibonacci(n-1))
  
```
### Code



``` python
main_menu = [
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu

math_sub_menu = [
    ["Swap", swap.test_swapNum],
    ["Fibonacci", fibonacci.fibonacci_tester],
    ["Factorials", factorial.recur_tester],
    ["IMP GCD", impgcd.gcd]
]

data_sub_menu = [
    ["Lists", listsandloops.tester],
]

visual_sub_menu = [
    ["Keypad", keypad.format_tester],
    ["Tree", tree.treefunc],
    ["Pattern", pattern.patternfunc]
]

oop_sub_menu = [
    ["OOP Palindrome", ooppalindrome.pali_tester],
    ["OOP Fibonacci", oopfib.fib_tester],
    ["OOP Factorial", oopfact.fact_tester],
    ["OOP GCD", oopgcd.gcd_tester]
]
```

#### Factorial Function with Classes

``` python
class Factorial:
  def __init__(self):
        self.factSeq = [1, 1]
  # Factorial of a number using recursion
  def __call__(self, n):
      if n == 1 or n == 0:
          return self.factSeq[n]
      else:
        fact_num = n * self(n-1)
        self.factSeq.append(fact_num)
      return self.factSeq[n]
  

def fact_tester():
  fact_of = Factorial()
  print(" 10 factorial is", fact_of(10))
  ```
  
#### Greatest Common Denominator 

``` python 
# Function to find the GCD of two Numbers
def findgcd(num1, num2):
    if num1 == 0:
        return num1
    while num2 != 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def gcd():
    a = int(input(" Enter the First Value for GCD: "))
    b = int(input(" Enter the Second Value for GCD: "))
    gcd = findgcd(a, b)
    print("\n GCD of {0} and {1} is: {2}".format(a, b, gcd))
    print()
```
``` python
class GCD:
  def __init__(self):
        self.gcdSeq = []
  # Factorial of a number using recursion
  def __call__(self, a, b):
      if a == 0:
          return a
      while b != 0:
        if a > b:
          a = a - b
        else:
            b = b - a
      return a # self.gcdSeq[a]

  

def gcd_tester():
  a = 342
  b = 114
  gcd_of = GCD()
  print("GCD of", a, "and", b, "is", gcd_of(a, b))
```

#### Palindrome OOP 

``` python
# import re


# class Palindrome:
#     # palindrome initializer method
#     def __init__(self, candidate):
#         # input values
#         self._candidate = candidate  # input string
#         self._length = len(candidate)  # input length
#         # analysis values
#         self._is_a_palindrome = False  # initialize status
#         self._az09 = re.sub(r'[^a-zA-Z0-9]', '', self._candidate)  # alpha numeric characters
#         self._analysis = []  # array of tests
#         self._tests = 0  # counter of tests performed
#         # evaluate for palindrome
#         self.is_palindrome()

#     # palindrome tester method
#     def is_palindrome(self):
#         c = self._az09
#         # Run loop from 0 to len/2 of string (middle is exit point)
#         tests = int(len(c) / 2)
#         for i in range(0, tests):
#             front = c[i];
#             back = c[len(c) - i - 1]
#             if front.lower() == back.lower():
#                 self.logger(front, back, True)
#                 self._tests += 1
#             else:
#                 self.logger(front, back, False)
#                 return
#         self._is_a_palindrome = True
#         return

#     # palindrome logging
#     def logger(self, front, back, result):
#         self._analysis.append({"test": self._tests, "front": front, "back": back, "result": result})

#     # getters follow
#     @property
#     def candidate(self):
#         return self._candidate

#     @property
#     def tests(self):
#         return self._tests

#     @property
#     def isPalindrome(self):
#         return self._is_a_palindrome

#     @property
#     def analysis(self):
#         return self._analysis

def pali_tester():
  # pali = Palindrome()
  # pali("uhefgsrbkjehiebihqet")
  print('\u001b[31;1mNot Currently Working\u001b[37;1m')
  ```
 #### Study Plan  
 
- Review Binary on Monday
- Rewatch first two chapters on CB videos Tueday
- Visit key concepts from last TRI on GitHub Wiki on Wednesday
- Review past MC quizzes and test to identify reoccurring mistakes on Thursday
- I want to refine my write-ups for create task along with creating a better video after previous feedback on friday

 #### Quiz 1 Corrections
 ![image](https://user-images.githubusercontent.com/89167149/165018606-aeea96fd-4ef8-4593-a5b6-05184524fdd4.png)
###### Q7
My Answer:B
Correct Answer:C
Reasoning: I became rusty at binary and did not review the proceces of translating in a long time, led to me making a mistake.
###### Q11
My Answer:A
Correct Answer:C
Reasoning: This was a very silly error as I had misread the question entirley
###### Q12
My Answer:C
Correct Answer:A
Reasoning: I failed to notice a crucial detail in the data provided as the infromation was stated previously 
###### Q21
My Answer:B
Correct Answer:C
Reasoning: The internet is a network not a data stream. I forgot the definiton for this one.
###### Q23
My Answer:D
Correct Answer:A
Reasoning: I forgot how intrusive website cookies really are 
###### Q36
My Answer:D
Correct Answer:A
Reasoning: I did not realize one of the attributes that was listed above would function the way it did
###### Q37
My Answer:D
Correct Answer:C
Reasoning: My logic was skewed though I may have clicked on the wrong one
###### 41
My Answer:B
Correct Answer:C
Reasoning: I was only looking at E if I looked at the destination I could have cut those off.
###### Q46
My Answer:A
Correct Answer:D
Reasoning: I forgot what a open protocal was. An open protocal is a protocal that is not bounded by any company.
###### Q49
My Answer:C
Correct Answer:D
Reasoning: I rushed for no reason, I became curious for what I got. Silly reading error
###### Q50
My Answer:D
Correct Answer:C
Reasoning: I rushed for no reason, I became curious for what I got. Silly reading error

#### Quiz 2 Corrections
###### Q18
My Answer:D
Correct:B
Reasoning: I made the mistake is differnciating the exponent function and multilplication
###### Q32
My Answer:A
Correct:C
Reasoning: The nature of bits allows for them to hold more than each direction 
###### Q35
My Answer:D
Correct:C
Reasoning: The program can only hold a certain number of bits so mine was wrong
###### Q36
My Answer:D
Correct:A
Reasoning: I made the mistake is differnciating the exponent function and multilplication

#### Quiz 3 Corrections
###### Q28
My Answer:D
Correct:B
Reasoning: I made the mistake is differnciating the exponent function and multilplication
###### Q32
My Answer:A
Correct:C
Reasoning: The nature of bits allows for them to hold more than each direction 
###### Q37
My Answer:D
Correct:C
Reasoning: The program can only hold a certain number of bits so mine was wrong
###### Q39
My Answer:D
Correct:A
Reasoning: I made the mistake is differnciating the exponent function and multilplication
 
 
 
 ```
  
                   
## Code / Runtime Links

[GitHub Repository](https://github.com/AkhilNandhakumar/Guython)

[Replit - Menus](https://replit.com/@somaditya1/CSP3#main.py)

## Replit Embed
<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@somaditya1/CSP3?embed=true">

