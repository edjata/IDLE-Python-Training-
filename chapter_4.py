Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print("Hello, world"{)
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'

print("Hello, World!")
      
Hello, World!
1 + 1
      
2
print("hello)
      
SyntaxError: unterminated string literal (detected at line 1)
print(Hello, World)
      
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(Hello, World)
NameError: name 'Hello' is not defined
f_name = input("First Name: ")
      
First Name: Empress
l_name = intput("Last Name: ")
      
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l_name = intput("Last Name: ")
NameError: name 'intput' is not defined. Did you mean: 'input'?
l_name = input("Last Name: ")
      
Last Name: Djata
full_name = f_name + " " + l_name
      
print(full_name)
      
Empress Djata
greeting = "Hello, World"
      
print(greeting)
      
Hello, World
greet = "Hello, "
      
print(greet + full_name)
      
Hello, Empress Djata

























print(Greet)
      
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(Greet)
NameError: name 'Greet' is not defined. Did you mean: 'greet'?
1 + 1
      
2
help
      
Type help() for interactive help, or help(object) for help about object.
help()
      
Welcome to Python 3.13's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.13/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q", "quit" or "exit".

help> q

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.

=============================== RESTART: Shell ==============================
phrase = "Hello, World"
      
print(phrase)
      
Hello, World
print(f"{}", phrase)
      
SyntaxError: f-string: valid expression required before '}'
print(f"This is {phrase}")
      
This is Hello, World
s = 3600
      
seconds = 3600
      
seconds_per_hour = 3600
      
phrase
      
'Hello, World'
s
      
3600
seconds
      
3600
print(phrase)!
      
SyntaxError: invalid syntax
x = 2
      
y = '2'
      
print(x)
      
2
print(y)
      
2
x
      
2
y
      
'2'
print
      
<built-in function print>
# This is a note
      
print("{#1")
      
{#1
print('#1')
#1
##print
type("Hello, world")
<class 'str'>
type(phrase)
<class 'str'>
string1 = "Hello, world"
string2 = "1234"
string3 = "We're #1"
string4 = 'I said, "Put it over by the llama."'
text = "She said, "What time is it?""
SyntaxError: invalid syntax
len("abc")
3
letters = "abc"
num_letters = len(letters)
paragraph = "This will be a short story about nothing\
but I will continue to write on an on just to see how this works.\
I can write ansd write and write just using a backslash at the end of \
each line to continue write"
print(paragraph)
This will be a short story about nothingbut I will continue to write on an on just to see how this works.I can write ansd write and write just using a backslash at the end of each line to continue write
long_string = "This multiline string is\
displayed on one line"
print(long_string)
This multiline string isdisplayed on one line
para2 = ""This will test the multiline string\
SyntaxError: invalid syntax
para2 = """this is a test to see what happenes"""
print(para2)
this is a test to see what happenes
para2[3]
's'
para2[-1]
's'
para2[-2]
'e'
user_input = input("Enter Text: ")
Enter Text: Empress Djata
final_index = len(user_input) - 1
final_index
12
last_char = user_input[final_index]
last_char\

e
SyntaxError: multiple statements found while compiling a single statement
last_char
'a'
last_char -2
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    last_char -2
TypeError: unsupported operand type(s) for -: 'str' and 'int'
last_char = user_input[final_index] - 2
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    last_char = user_input[final_index] - 2
TypeError: unsupported operand type(s) for -: 'str' and 'int'
last_char2 = user_input[-2]
last_char2
't'
fav = "apple pie"
first_3_char = fav[0] + fav[1] + fav[2]
first_3_char
'app'
fav[0:3]
'app'
fav[3:]
'le pie'
fav[3]
'l'
fav[0:5]
'apple'
fav[:5]
'apple'
fav[:]
'apple pie'
fav[:14]
'apple pie'
fav[13:15]
''
fav[-9:-6]
'app'
fav[-9:-1]
'apple pi'
fav[-9:0]
''
fav[-9:]
'apple pie'
word = "goal"
word[0]
'g'
word[0] = "f"
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    word[0] = "f"
TypeError: 'str' object does not support item assignment
word = 'f' + word[1:]
word
'foal'
namegame = "empie"
len(namegame)
5
print(namegame +"
      
SyntaxError: unterminated string literal (detected at line 1)
print(namegame+word)
      
empiefoal
print(namegame + " " + word)
      
empie foal
word1 = namegame + word
      
print(word1)
      
empiefoal
word2 = namegame + ' ' + word
      
print(word2)
      
empie foal
word3 = "bazinga"
      
print(word3[2:5])
      
zin
print(word3[2:6])
      
zing
word.upper()
      
'FOAL'
'empress'.upper()
      
'EMPRESS'
'Emp DjAtA'.lower()
      
'emp djata'
loud_voice = "Can you hear me yet?"
      
loud_voice.upper()
      
'CAN YOU HEAR ME YET?'
len(loud_voice)
      
20
w1 = loud_voice
      
w2 = loud_voice
      
w1
      
'Can you hear me yet?'
w1.rstrip()
      
'Can you hear me yet?'
w1
      
'Can you hear me yet?'
loud_voice.rstrip()
      
'Can you hear me yet?'
w1.upper()
      
'CAN YOU HEAR ME YET?'
w1.lstrip()
      
'Can you hear me yet?'
w1
      
'Can you hear me yet?'
w1.strip()
      
'Can you hear me yet?'
w3 = 'e  m  p   r   e  ss'
      
w3
      
'e  m  p   r   e  ss'
w3.strip()
      
'e  m  p   r   e  ss'
jname = "Jean-luc Picard      "
      
jname
      
'Jean-luc Picard      '
jname.rstrip()
      
'Jean-luc Picard'
jname2 = "      Jean-luc Picard     "
      
jname2
      
'      Jean-luc Picard     '
jname3 = jname2
      
jname3
      
'      Jean-luc Picard     '
jname2.lstrip()
      
'Jean-luc Picard     '
jname3
      
'      Jean-luc Picard     '
jname2.rstrip()
      
'      Jean-luc Picard'
jname2
      
'      Jean-luc Picard     '
jname2.lstrip().rstrip()
      
'Jean-luc Picard'
jname2
      
'      Jean-luc Picard     '
jname2.strip()
      
'Jean-luc Picard'
jname2 = jname2.lstrip().rstrip()
      
jname2
      
'Jean-luc Picard'
starship = "Enterprise"
      
starship.startswith('en')
      
False
answer = starship.capitalize("En")
      
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    answer = starship.capitalize("En")
TypeError: str.capitalize() takes no arguments (1 given)
answerme1 = starship.startswith("En")
      
answerme1
      
True
starship.endswith("rise")
      
True
starship.endwith("risE")
      
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    starship.endwith("risE")
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
starship
      
'Enterprise'
starship.endwith("Rise")
      
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    starship.endwith("Rise")
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
starship.endswith("Rise")
      
False
pname = "Picard"
      
pname
      
'Picard'
pname.upper()
      
'PICARD'
pname
      
'Picard'
pname = pname.upper()
      
pname
      
'PICARD'
starship2 = starship
      
starship2.
      
SyntaxError: invalid syntax
starship.capitalize()
      
'Enterprise'
starship2
      
'Enterprise'
starship2.casefold()
      
'enterprise'
starship2
      
'Enterprise'
starship2.center()
      
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    starship2.center()
TypeError: center expected at least 1 argument, got 0
starship2.center(4)
      
'Enterprise'
starship2.count()
      
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    starship2.count()
TypeError: count expected at least 1 argument, got 0
s1 = starship2
      
s1.encode()
      
b'Enterprise'
s1.expandtabs(tabsize=8)
      
'Enterprise'
s1.find('erp')
      
3
s1.find('e')
      
3
s1.find('n'
        )
      
1
s1.capitalize("E")
      
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    s1.capitalize("E")
TypeError: str.capitalize() takes no arguments (1 given)
s1.find("E")
      
0
s1.format(*args, sep='   ', end='\n\n', file=None, false=False)
      
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    s1.format(*args, sep='   ', end='\n\n', file=None, false=False)
NameError: name 'args' is not defined
s1.format(*s1, sep='   ', end='\n\n', file=None, false=False)
      
'Enterprise'
s1.swapcase()
      
'eNTERPRISE'
"Animals".lower()
      
'animals'
"Badger".lower()
      
'badger'
"Honey Bee".lower()
      
'honey bee'
"Honeybadger".lower()
      
'honeybadger'
"Animals".upper()
      
'ANIMALS'
"Badger".upper()
      
'BADGER'
"Honey Bee".upper()
      
'HONEY BEE'
"Honeybadger".upper()
      
'HONEYBADGER'
string1 = " Filet Mignon"
      
string1.lstrip()
      
'Filet Mignon'
string2 = "Brisket "
      
string2.rstrip()
      
'Brisket'
string2 = "Brisket ".strip()
      
string2
      
'Brisket'
string3 = " Cheeseburger "
      
string3.strip()
      
'Cheeseburger'
string1 = "Becomes"
      
string1.startswith('be')
      
False
string2 = "becomes"
      
string2 = "becomes".startswith('be')
      
string2
      
True
string2 = "becomes"
      
string2.startswith('be')
      
True
string3 = "BEAR"
      
string4 = " bEautiful"
      
string3.startswith('be')
      
False
string4.startswith('be')
      
False
string3.startswith('be') or string4.startswith('be')
      
False
string3.startswith('be') and string4.startswith('be')
      
False
string2.startswith('be') or string4.startswith('be')
      
True
string2.startswith('be') and string4.startswith('be')
      
False
string4.startswith('be') or string2.startswith('be')
      
True
input()
      

''
input("ENTER TEXT: ")
      
ENTER TEXT: Hello world
'Hello world'
p1 = "Hey, what's up?"
      
u_input = input(p1 + ' ')
      
Hey, what's up? nothing really just chilling
print("You said:", u_input)
      
You said: nothing really just chilling
r1 = input("What sould I shout? ")
      
What sould I shout? Fuck Off bitch
s_r1 = r1.upper()
      
print("Well, ", s_r1)
      
Well,  FUCK OFF BITCH
user1 = input("Enter Text: ")
      
Enter Text: Hello everyone on earth none left
print(user1)
      
Hello everyone on earth none left
print(user1.lower())
      
hello everyone on earth none left
user1.count()
      
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    user1.count()
TypeError: count expected at least 1 argument, got 0
len(user1)
      
33
first_letter.py
      
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    first_letter.py
NameError: name 'first_letter' is not defined

= RESTART: C:/Users/Duron Walton/Desktop/E/IDLE Python Training/first_letter.py
Tell me your password: empress1
E

= RESTART: C:/Users/Duron Walton/Desktop/E/IDLE Python Training/first_letter.py
Tell me your password: empress1
The first letter you entered was E

= RESTART: C:/Users/Duron Walton/Desktop/E/IDLE Python Training/first_letter.py
Tell me your password: empressdj1
The first letter you entered was:  E
num = "2"
      
num + num
      
'22'
num = "12"
      
num * 3
      
'121212'
3 * num
      
'121212'
3 * int(num)
      
36
"12" * "3"
      
Traceback (most recent call last):
  File "<pyshell#251>", line 1, in <module>
    "12" * "3"
TypeError: can't multiply sequence by non-int of type 'str'
"3" * 3
      
'333'
"3" + 3
      
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    "3" + 3
TypeError: can only concatenate str (not "int") to str
num = input("Enter a number to be doubled: ")
      
Enter a number to be doubled: 5
doubled_num * 2
      
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    doubled_num * 2
NameError: name 'doubled_num' is not defined
num = int(input("Enter a number to be doubled: "))
      
Enter a number to be doubled: 5
doubled_num * 2
      
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    doubled_num * 2
NameError: name 'doubled_num' is not defined
doubled_num = num * 2
      
print(doubled_num)
      
10
num = input("Enter a number to be doubled: ")
      
Enter a number to be doubled: 5
doubled_num = num * 2
      
print(doubled_num)
      
55
int('12')
      
12
float('13')
      
13.0
num = int(input("Enter a number to be doubled: "))
      
Enter a number to be doubled: 6
doubled_num = num * 2
      
print(doubled_num)
      
12
num = float(input("Enter a number to be doubled: "))
      
Enter a number to be doubled: 8
doubled_num = num * 2
      
print(doubled_num)
      
16.0
num_pancakes = 10
      
"I am going to eat " + num_pancakes + " pancakes."
      
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    "I am going to eat " + num_pancakes + " pancakes."
TypeError: can only concatenate str (not "int") to str
"I am going to eat " + int(pancakes) + " pancakes."
      
Traceback (most recent call last):
  File "<pyshell#273>", line 1, in <module>
    "I am going to eat " + int(pancakes) + " pancakes."
NameError: name 'pancakes' is not defined
"I am going to eat " + str(pancakes) + " pancakes."
      
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    "I am going to eat " + str(pancakes) + " pancakes."
NameError: name 'pancakes' is not defined
"I am going to eat " + str(num_pancakes) + " pancakes."
      
'I am going to eat 10 pancakes.'
"I am going to eat " + str(10) + " pancakes."
      
'I am going to eat 10 pancakes.'
total_pancakes = 10
      
pancakes_eaten = 5
      
"Only " + str(total_pancakes - pancakes_eaten) + " pancakes left."
      
'Only 5 pancakes left.'
str(print)
      
'<built-in function print>'
str(int)
      
"<class 'int'>"
str(float)
      
"<class 'float'>"
int_string = ("123")
      
int_string
      
'123'
int_string = int(int_string)
      
int_string
      
123
print(int_string * 3)
      
369
print(gloat(int_string) * 4)
      
Traceback (most recent call last):
  File "<pyshell#288>", line 1, in <module>
    print(gloat(int_string) * 4)
NameError: name 'gloat' is not defined. Did you mean: 'float'?
print(float(int_string) * 4)
      
492.0
str_obj = "12"
      
int_obj = 12
      
print(str_obj + str(int_obj))
      
1212
num1 = input("Enter 1st num: ")
      
Enter 1st num: 12
num2 = input("Enter 2nd num: ")
      
Enter 2nd num: 33
num_ans = num1 * num2
      
Traceback (most recent call last):
  File "<pyshell#295>", line 1, in <module>
    num_ans = num1 * num2
TypeError: can't multiply sequence by non-int of type 'str'
"I am going to eat " + str(num_pancakes) + " pancakes."
      
'I am going to eat 10 pancakes.'

num1 = int(input("Enter 1st num: "))
      
Enter 1st num: 12
num2 = int(input("Enter 2nd num: "))
      
Enter 2nd num: 33
num_ans = num1 * num2
      
print("The product of " + num1 + " and " + num2 + " is " + num_ans)
      
Traceback (most recent call last):
  File "<pyshell#301>", line 1, in <module>
    print("The product of " + num1 + " and " + num2 + " is " + num_ans)
TypeError: can only concatenate str (not "int") to str
print("The product of " + str(num1) + " and " + str(num2) + " is " + str(num_ans))
      
The product of 12 and 33 is 396
print("The product of " + str(num1) + " and " + str(num2) + " is " + str(num_ans + "."))
      
Traceback (most recent call last):
  File "<pyshell#303>", line 1, in <module>
    print("The product of " + str(num1) + " and " + str(num2) + " is " + str(num_ans + "."))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("The product of " + str(num1) + " and " + str(num2) + " is " + str(num_ans) + ".")
      
The product of 12 and 33 is 396.
name = "Zaphod"
      
heads = 2
      
arms = 3
      
print(name, "has", str(heads), "heads and", str(arms), "arms")
      
Zaphod has 2 heads and 3 arms
print(name + "has" + str(heads) + "heads and" + str(arms) + "arms")
      
Zaphodhas2heads and3arms
f"{name} has {heads} heads and {arms} arms"
      
'Zaphod has 2 heads and 3 arms'
f"{name} has {heads} heads and {arms} arms"
      
'Zaphod has 2 heads and 3 arms'
n = 3
      
m = 4
      
f"{n} times {m} is {n*m}"
      
'3 times 4 is 12'

= RESTART: C:/Users/Duron Walton/Desktop/E/IDLE Python Training/math1.py

= RESTART: C:/Users/Duron Walton/Desktop/E/IDLE Python Training/math1.py
yn = 3

m = 4

f"{n} times {m} is {n*m}"
      
SyntaxError: multiple statements found while compiling a single statement
"{} has {} heads and {} arms".format(name, heads, arms)
      
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    "{} has {} heads and {} arms".format(name, heads, arms)
NameError: name 'name' is not defined
name = "Empress"
      
"{} has {} heads and {} arms".format(name, heads, arms)
      
Traceback (most recent call last):
  File "<pyshell#318>", line 1, in <module>
    "{} has {} heads and {} arms".format(name, heads, arms)
NameError: name 'heads' is not defined
heads = 2
      
arms = 3
      
SyntaxError: multiple statements found while compiling a single statement
heads = 2
      
arms = 3
      
"{} has {} heads and {} arms".format(name, heads, arms)
      
'Empress has 2 heads and 3 arms'
weight = 0.2
      
weight
      
0.2
animal ="newt"
      
animal
      
'newt'
print(str(weight), " kg is the weight of the ", animal, ".")
      
0.2  kg is the weight of the  newt .
print(str(weight), "kg is the weight of the", animal, ".")
      
0.2 kg is the weight of the newt .
"{} kg is the weight of the {}".format(weight, animal)
      
'0.2 kg is the weight of the newt'
print(f"{weight} is the weight of the {animal}")
      
0.2 is the weight of the newt
phrase = "the surprise is in here somewhere"
      
phrase.find("surprise")
      
4
phrase.find("eyjafjallajökull")
      
-1
"the surprise is in here somewhere".find("surprise")
      
4
"the surprise is in here somewhere".find("SURPRISE")
      
-1
"I put a string in your string".find("string")
      
8
"My number is 555-555-5555".find(str(5))
      
13
"My number is 555-555-5555".find("5")
      
13
 my_story = "I'm telling you the truth; nothing but the truth!"
      
SyntaxError: unexpected indent
my_story = "I'm telling you the truth; nothing but the truth!"
      
my_story.replace("the truth", "lies")
      
"I'm telling you lies; nothing but lies!"
my_story
      
"I'm telling you the truth; nothing but the truth!"
my_story = my_story.replace("the truth", "lies")
      
my_story
      
"I'm telling you lies; nothing but lies!"
text = "some of the stuff"
...       
>>> new_text = text.replace("some of", "all")
...       
>>> new_text
...       
'all the stuff'
>>> new_text = new_text.replace("stuff", "things")
...       
>>> new_text
...       
'all the things'
>>> "AAA".find("a")
...       
-1
>>> text1 = "Somebody said something to Samantha.".replace("s", "x")
...       
>>> text1
...       
'Somebody xaid xomething to Samantha.'
>>> text2 = text1.replace("S", "X")
...       
>>> text2
...       
'Xomebody xaid xomething to Xamantha.'
>>> user1 = input("Enter text: ")
...       
Enter text: Hello everyone how are you doing today?
>>> user1.find("?")
...       
38
>>> 
= RESTART: C:/Users/Duron Walton/Desktop/E/IDLE Python Training/translate.py
Enter some text: I like to eat eggs and spam.
I like to e4t eggs 4nd sp4m.
>>> 
= RESTART: C:/Users/Duron Walton/Desktop/E/IDLE Python Training/translate.py
Enter some text: I like to eat eggs and spam.
I 1ik3 70 347 3gg5 4nd 5p4m.
