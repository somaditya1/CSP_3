from tt0 import patterns, swap, tree
from tt1 import loops, fibonacci, factorial
from tt2 import palindrome, factorialC, seq, consec

    
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Swapping", swap.numberSwapper],
    ["Smaller # 1st", swap.lessNumSwap],
]

sub_menu0 = [
    ["Animation", patterns.smile],
    ["Diamond", patterns.diamond],
    ["Tree", tree.treefunc],
]

sub_menu1 = [
    ["List Printer", loops.tester],
    ["Fibonacci", fibonacci.fibonacci],
]

sub_menu2 = [
  ["Factorial OOP", factorialC.factorial_print],
  ["Factorial", factorial.tester1],
  ["Sequential Sum (OOP)", consec.consec_print],
  ["Sequential Sum (Imperative)", seq.seq_sum],
]

sub_menu3 = [
  ["Palindrome Tester", palindrome.pali_tester],
]

# Menu banner is typically defined by menu owner
border1 = "«" * 25
border2 = "»" * 25 
banner = f"\n{border1}\nSelect An Option\n{border2}"



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
    menu_list.append(["Animations (TT0)", submenu0])
    menu_list.append(["Lists & Fibonacci (TT1)", submenu1])
    menu_list.append(["Math (TT2)", submenu2])
    menu_list.append(["Palindrome", submenu3])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Swap Submenu" + banner
    buildMenu(title, sub_menu)

def submenu0():
    title = "TT0 Submenu" + banner
    buildMenu(title, sub_menu0)

def submenu1():
    title = "TT1 Submenu" + banner
    buildMenu(title, sub_menu1)

def submenu2():
    title = "TT2 Submenu" + banner
    buildMenu(title, sub_menu2)

def submenu3():
    title = "Palindrome Submenu" + banner
    buildMenu(title, sub_menu3)

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
        print(key, '─', value[0])

    # get user choice
    choice = input("Type your choice: ")

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