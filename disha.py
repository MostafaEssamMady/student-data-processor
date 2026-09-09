
#coments

#--------------------------
#type()
# all data in python is object
#--------------------------
print(type(10))#int => intrger
print(type(199))#int => intrger
print(type(-80))#int => intrger

print(type(10.888))# float => floating point number
print(type(1.90))# float => floating point number
print(type(-67.899))# float => floating point number

print(type("mostafa")) # str => string

print(type([1,4,7,8]))# list =>list

print(type((3,8,9,5))) # tuple =>Tuple

print(type({"one":1, "two":2})) # dict => Dictionary

print(type(2==9)) # bool => Boolen

#----------------------------------------

#-- Variables(1)--

#----------------------------------------

# syntax => [ variable Nume ] [Assignment Oprator] [value]
#
# Nume convention and Rules
# [1] can start with ( a-z A-Z) or underscore
# [2] you cannot with Num or special characters
# [3] can include (0-9) underscore
# [4] cannot include special characters 
# [5] Num is not like name [ case sensitive]
#---------------------------------------------

name = "mostafa essam" # single word => normal
myName = "mostafa essam" # two words => camel case
my_name = "mostafa essam" # two words => snke_case

print(name)
print(myName)
print(my_name)

#----------------------
# --Variables(2)--
#----------------------
# Source code : original code you write it in computer 
# Translation : converting source code into machine language 
# Compilation : translate code before run time 
# Run-Time : period app take to executing commands
# Interpreted : cod translated on the fly during Execution
#----------------------------------------------------------------------
#   دى كلمات المحجوزه فى لغهhelp("keywords") 

#Here is a list of the Python keywords.  Enter any keyword to get more help.

# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not

#-------------------------------------------------
# Escape sequences characters 
# \b => Back space
# \newline => Escape new line +\
# \\ => escape back slash
# \' => escape  single slash
# \" => escape  double  slash
# \n => line feed 
# \r => carriage return
# \t => horizontal tap
# \xhh => character hex value
#---------------------------------------
 
 # Back space
print("hello\bworld")   # will remove o

# Escape new line + back slash
print("hello \
i love \
python")

# escape back slash
print("i love back slash \\")

# escape  single slash
print('i love mostafa \'marwa\' ')

# escape  double  slash
print("i love mostafa \"marwa\" ")

# line feed
print("iam mostafa \n iam19")

# carriage return
print("12345678 \r mostafa")

# horizontal tap
print("mostafa \t essam ")

# character hex value
print("\x4d \x4f \x53")

#------------------------------------
#-- concatenation --
#------------------------------------

msg = "i love"
lang = "mostafa"
print(msg + "  " + lang)


full = msg + "  " + lang
print(full)

a = "mostafa \
essam \
mady"

b = "20\
0\
7"

print(a + "\n" + b)

# ----------------
# -- Strings --
# ----------------

myStringOne = 'This is Single Quote'
myStringTwo = "This is Double Quotes"

print(myStringOne)
print(myStringTwo)

myStringThree = 'This is Single Quote "Test"'
myStringFour = "This is Double Quotes 'Test'"

print(myStringThree)
print(myStringFour)

myStringFive = '''First
Second 'Test' "Test"
Third'''

myStringSix = """First
Second "Test" \\\ 'Test'
Third"""

print(myStringFive)
print(myStringSix)

# ---------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------

# Indexing ( Access Single Item )

myString = "I Love Python"

print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t

print(myString[-1])  # Index -1 => First Character From End => n
print(myString[-6])  # Index -6 => 6th Character From End   => p

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
print(myString[:])  # Full Data

print(myString[0::1])  # Full Data
print(myString[::1])  # Full Data

print(myString[::2])
print(myString[::3])


# ---------------------
# -- Strings Methods ONE --
# ---------------------

# strip() rstrip() lstrip()   =>  بتشيل المسافات 

a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#####I Love Python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()  => بتحول كل حرف اول كلمه لى كابتل 

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()  

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill      =>   بتزود صفر عشان يبقا كله متساوى

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper()   =>  بتحول كلمه كلها لى كابتل 


g = "mostafa"

print(g.upper())

# lower()  =>  بتحول كلمه كلها لى اسمول 

h = "MOSTAFA"

print(h.lower())


# ---------------------
# -- Strings Methods TWO --
# ---------------------

# split()    =>   list  بتعمل اى بترجع كل حاجه لى 
#  rsplit()    =>   list  بتعمل اى بترجع كل حاجه لى 


a = "I Love Python and PHP and MySQL"
print(a.split())

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3))

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))

# center()

e = "mostafa"
print(e.center(9))  # Spaces
print(e.center(9, "#"))  # Hashes
print(e.center(15, "@"))  # @

# count()   =>   بتقولك كلمه دى موجوده كام مره فى جمله

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # 2 PHP Words
print(f.count("PHP", 0, 25))  # Only One PHP Word

# swapcase()  =>  بتعمل اى بتعمل لو حرف او كلمه مكتوبه كابتل يحولها لى سمول والعكس برده

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()   =>  بتقولو لو حرف كذا  بدا بي يقةلى اه  ولو مبداش يقولى لا 

i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# endswith()   =>   startswith() عكس  فوق بدايه كلمه تحت بسال نهايه كلمه 

j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))


# ---------------------
# -- Strings Methods three --
# ---------------------

# index(SubString, Start, End)

a = "I Love Python"
# print(a.index("P"))  # Index Number 7
# print(a.index("P", 0, 10))  # Index Number 7
# print(a.index("P", 0, 5))  # Through Error

# find(SubString, Start, End)

b = "I Love Python"
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

# rjust(Width, Fill Char) ljust(Width, Fill Char)

c = "mostafa"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "mostafa"
print(d.ljust(10))
print(d.ljust(10, "#"))

# splitlines()

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

# expandtabs()  =>  بتحدد التاب  لو قولت اتنين تعمل اتنين تاب بس 

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))

#   istitle()      =>    ولا  يا اه او لاtitle انت هنا بستال هل ده 

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())    
print(two.istitle())

three = " "
four = ""
print(three.isspace())   # =>    ولا   يا اه او لاscpace  انت هنا بستال هل ده 
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())    # =>    ولا   يا اه او لا lower  انت هنا بستال هل ده 
print(six.islower())

seven = "mostafa_essam"
eight = "disha3007"
nine = "disha--essam"

print(seven.isidentifier())   # =>     ولا   يا اه او لا identifier  انت هنا بستال هل ده  يعنى ينفع يكون متغبر 
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())

# ---------------------
# -- Strings Methods four --
# ---------------------

# replace(Old Value, New Value, Count)   =>  بتبدل الكلمه لى انت عايزها لى كلمه تانيه انت تتكتبها ليه 

a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# join(Iterable)  =>

myList = ["mostafa", "essam", "mady"]
print("-".join(myList))
print(" ".join(myList))
print(", ".join(myList))
print(type(", ".join(myList)))

# ------------------------
# -- Strings Formatting --
# ------------------------

name = "mostafa"
age = 19
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: %s" % "mostafa")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

# %s => String
# %d => Number
# %f => Float

n = "mostafa"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: %d" % myNumber)  # => 10
print("My Number is: %f" % myNumber)    # => 10.00000000
print("My Number is: %.2f" % myNumber)  # => 10.00

# Truncate String

myLongString = "Hello Peoples of DISHA Web School I Love You All"
print("Message is : %s" % myLongString)    #  =>  Hello Peoples of DISHA Web School I Love You All
print("Message is : %.5s" % myLongString)  #  =>   Hello

# ---------------------------------
# -- Strings Formatting New Ways --
# ---------------------------------

name = "mostafa"
age = 19
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: {}".format("mostafa"))
print("My Name is: {}".format(name))
print("My Name is: {} My Age: {}".format(name, age))
print("My Name is: {:s} & My Age: {:d} & Rank is: {:f}".format(name, age, rank))

# {:s} => String
# {:d} => Number
# {:f} => Float

n = "mostafa"
l = "Python"
y = 10

print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: {:d}".format(myNumber))   # => 10
print("My Number is: {:f}".format(myNumber))    # => 10.0000000
print("My Number is: {:.2f}".format(myNumber))    # => 10.00

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {}".format(myLongString))   # =>  Message is Hello Peoples of Elzero Web School I Love You All
print("Message is {:.5s}".format(myLongString))    # =>  Message is Hello
print("Message is {:.13s}".format(myLongString))    # =>  Message is Hello Peoples

# Format Money

myMoney = 500162350198

print("My Money in Bank Is: {:d}".format(myMoney))  # => My Money in Bank Is: 500162350198
print("My Money in Bank Is: {:_d}".format(myMoney))  # => My Money in Bank Is: 500_162_350_198
print("My Money in Bank Is: {:,d}".format(myMoney))  # => My Money in Bank Is: 500,162,350,198

# ReArrange Items

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))  # => Hello 10 20 30
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))  #  => Hello 20 30 10
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))  #  =>  Hello 30.000000 10.000000 20.000000
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))   #  =>  Hello 30.00 10.0000 20.00000

# Format in Version 3.6+

myName = "mostafa"
myAge = 19

print("My Name is : {myName} and My Age is : {myAge}")   #  My Name is : {myName} and My Age is : {myAge}
print(f"My Name is : {myName} and My Age is : {myAge}")  #  My Name is : mostafa and My Age is : 19


# -------------
# -- Numbers --
# -------------

# Integer

print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# Float

print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex

myComplexNumber = 5+6j

print(type(myComplexNumber))

print("Real Part Is: {}".format(myComplexNumber.real))
print("Imaginary Part Is: {}".format(myComplexNumber.imag))

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)
#print(int(10+9j))   error

# --------------------------
# -- Arithmetic Operators --
# --------------------------
# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division
# --------------------------

# Addition

print(10 + 30)  # 40
print(-10 + 20)  # 10
print(1 + 2.66)  # 3.66
print(1.2 + 1.2)  # 2.4

# Subtraction

print(60 - 30)  # 30
print(-30 - 20)  # -50
print(-30 - -20)  # -10
print(5.66 - 3.44)  # 2.22

# Multiplication

print(10 * 3)  # 30
print(5 + 10 * 100)  # 1005
print((5 + 10) * 100)  # 1500

# Division

print(100 / 20)  # 5.0
print(int(100 / 20))  # 5

# Modulus

print(8 % 2)  # 0
print(9 % 2)  # 1
print(20 % 5)  # 0
print(22 % 5)  # 2

# Exponent

print(2 ** 5)  # 32
print(2 * 2 * 2 * 2 * 2)  # 32
print(5 ** 4)  # 625
print(5 * 5 * 5 * 5)  # 625

# Floor Division

print(100 // 20)  # 5
print(119 // 20)  # 5
print(120 // 20)  # 6
print(140 // 20)  # 7
print(142 // 20)  # 7

# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomeList)  # Whole List
print(myAwesomeList[1])  # "Two"
print(myAwesomeList[-1])  # True
print(myAwesomeList[-3])  # 1

print(myAwesomeList[1:4])  # ['Two', 'One', 1]
print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomeList[::2])  # ['One', 'One', 100.5]

print(myAwesomeList)

myAwesomeList[1] = 2
print(myAwesomeList)
myAwesomeList[-1] = False
print(myAwesomeList)
myAwesomeList[0:3] = ["A"]
print(myAwesomeList)

# -------------------
# -- Lists Methods (1) --
# -------------------

# append()

myFriends = ["mostafa", "yousef", "marwa"]
myOldFriends = ["mohaned", "yahia", "momen"]

myFriends.append("disha")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])

# extend()

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# remove()

x = [1, 2, 3, 4, 5, "disha", True, "disha", "disha"]
x.remove("disha")
print(x)

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True)
print(y)

# reverse()

z = [10, 1, 9, 80, 100, "disha", 100]
z.reverse()
print(z)

# -------------------
# -- Lists Methods(2) --
# -------------------

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()

b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index()

e = ["disha", "marwa", "yousef", "mohaned", "momen", "yahia"]
print(e.index("disha"))

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")

print(f)

# pop()

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))

# -----------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# -----------------------------

# Tuple Syntax & Type Test

myAwesomeTupleOne = ("mostafa", "disha")
myAwesomeTupleTwo = "mostafa", "disha"

print(myAwesomeTupleOne)
print(myAwesomeTupleTwo)

print(type(myAwesomeTupleOne))
print(type(myAwesomeTupleTwo))

# Tuple Indexing

myAwesomeTupleThree = (1, 2, 3, 4, 5)
print(myAwesomeTupleThree[0])
print(myAwesomeTupleThree[-1])
print(myAwesomeTupleThree[-3])

# Tuple Assign Values

myAwesomeTupleFour = (1, 2, 3, 4, 5)
# myAwesomeTupleFour[2] = "Three"
# print(myAwesomeTupleFour)  # 'tuple' object does not support item assignment

# Tuple Data

myAwesomeTupleFive = ("mostafa", "disha", 1, 1, 2, 3, 100.5, True)
print(myAwesomeTupleFive[1])
print(myAwesomeTupleFive[-1])


# -----------
# -- Tuple --
# -----------

# Tuple With One Element

myTuple1 = ("mostafa",)
myTuple2 = "mostafa",

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

print(len(myTuple1))
print(len(myTuple2))

# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b

print(c)
print(d)

# Tuple, List, String Repeat (*)

myString = "mostafa"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# Methods => count()

a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))

# Methods => index()

b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"The Position of Index Is: {b.index(7)}")

# Tuple Destruct

a = ("A", "B", 4, "C")

x, y, _, z = a

print(x)
print(y)
print(z)


# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# Not Ordered And Not Indexed

mySetOne = {"mostafa", "essam", 100}
print(mySetOne)
# print(mySetOne[0])

# Slicing Cant Be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

# Has Only Immutable Data Types

# mySetThree = {"mostafa", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = {"mostafa", 100, 100.5, True, (1, 2, 3)}

print(mySetThree)

# Items Is Unique

mySetFour = {1, 2, "mostafa", "One", "mostafa", 1}
print(mySetFour)


# -----------------
# -- Set Methods one--
# -----------------

# clear()

a = {1, 2, 3}
a.clear()
print(a)

# union()

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}

print(b | c)
print(b.union(c, x))

# add()

d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)

# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)

# remove()

g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)
print(g)

# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)

# pop()

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())

# update()

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)

print(j)


# -----------------
# -- Set Methods two --
# -----------------

# difference()

a = {1, 2, 3, 4}
b = {1, 2, 3, "mostafa", "essam"}
print(a)
print(a.difference(b))  # a - b
print(a)

print("=" * 40)  # Separator

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, "mostafa", "essam"}
print(c)
c.difference_update(d)  # c - d
print(c)

print("=" * 40)  # Separator

# intersection()

e = {1, 2, 3, 4, "X", "mostafa"}
f = {"mostafa", "X", 2}
print(e)
print(e.intersection(f))  # e & f
print(e)

print("=" * 40)  # Separator

# intersection_update()

g = {1, 2, 3, 4, "X", "mostafa"}
h = {"mostafa", "X", 2}
print(g)
g.intersection_update(h)  # g & h
print(g)

print("=" * 40)  # Separator

# symmetric_difference()

i = {1, 2, 3, 4, 5, "X"}
j = {"mostafa", "essam", 1, 2, 4, "X"}
print(i)
print(i.symmetric_difference(j))  # i ^ j
print(i)

print("=" * 40)  # Separator

# symmetric_difference_update()

k = {1, 2, 3, 4, 5, "X"}
l = {"mostafa", "essam", 1, 2, 4, "X"}
print(k)
k.symmetric_difference_update(l)  # k ^ l
print(k)


# -----------------
# -- Set Methods three--
# -----------------

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))  # True
print(a.issuperset(c))  # False

print("=" * 50)

# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False
print(d.issubset(f))  # True

print("=" * 50)

# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False
print(g.isdisjoint(i))  # True

# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary

user = {
  "name": "mostafa",
  "age": 19,
  "country": "Egypt",
  "skills": ["Html", "Css", "JS"],
  "rating": 10.5
}

print(user)
print(user['country'])
print(user.get("country"))

print(user.keys())
print(user.values())

# Two-Dimensional Dictionary

languages = {
  "One": {
    "name": "Html",
    "progress": "80%"
  },
  "Two": {
    "name": "Css",
    "progress": "90%"
  },
  "Three": {
    "name": "Js",
    "progress": "90%"
  }
}

print(languages)
print(languages['One'])
print(languages['Three']['name'])

# Dictionary Length

print(len(languages))
print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree
}

print(allFramework)

# ------------------------
# -- Dictionary Methods one --
# ------------------------

# clear()

user = {
  "name": "mostafa"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# update()

member = {
  "name": "mostafa"
}
print(member)
member["age"] = 19
print(member)
member.update({"country": "Egypt"})
print(member)

print("=" * 50)

# copy()

main = {
  "name": "mostafa"
}

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

# keys() + values()

print(main.keys())
print(main.values())


# ------------------------
# -- Dictionary Methods two --
# ------------------------

# setdefault()

user = {
  "name": "mostafa"
}
print(user)
print(user.setdefault("age", 19))
print(user)

print("=" * 40)

# popitem()

member = {
  "name": "mostafa",
  "skill": "PS4"
}
print(member)
member.update({"age": 19})
print(member.popitem())

print("=" * 40)

# items()

view = {
  "name": "mostafa",
  "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 19

print(allItems)

print("=" * 40)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

print(dict.fromkeys(a, b))


# -------------
# -- Boolean --
# -------------
# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------------------------

name = " "
print(name.isspace())

print("=" * 50)

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("=" * 50)

# True Values

print(bool("mostafa"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("=" * 50)

# False Values

print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))


# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 19
country = "Egypt"
rank = 10

print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print(age > 40 or country == "KSA" or rank > 20)  # False
print(age > 40 or country == "Egypt" or rank > 20)  # True

print(age > 16)  # True
print(not age > 16)  # Not True = False

