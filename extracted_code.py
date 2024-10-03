
# Prac_1a 
# Create a program that asks the user to enter their name and their age. Print out
#  a
#  message addressed to them that tells them the year that they will turn 100 years
#  old.
import datetime
name = input("Enter your name: ")
age = int(input("Enter your age: "))
currentyear = datetime.datetime.now().year
dob = currentyear - age
print(dob + 100)

# Prac_1b
#even or odd number
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Prac_1c
#fibonacci series
n = int(input("Enter a number: "))
first = 0
second = 1
for i in range(n):
    print(first)
    temp = first
    first = second
    second = second + temp

# Prac_1d
#reverse the user define value

def rev(n):
    reverse = 0
    while n > 0:
        reminder = n % 10
        reverse = (reverse * 10) + reminder
        n = n // 10
    return reverse

n = int(input("Enter a number: "))
reverse1 = rev(n)
print("Reverse number: ", reverse1)

# Prac_1e
#armstrong and palindrome

def Armstrong(n):
    temp = n
    result = 0
    while temp > 0:
        remainder = temp % 10
        result = remainder ** 3 + result
        temp = temp // 10
    if result == n:
        print(n, "is an Armstrong")
    else:
        print(n, "is not an Armstrong")

def Palindrome(n):
    temp = n
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = reverse * 10 + remainder
        temp = temp // 10
    if n == reverse:
        print(reverse, "is a Palindrome")
    else:
        print(reverse, "is not a Palindrome")

n = int(input("Enter a number: "))
Armstrong(n)
Palindrome(n)

# Prac_1f
#Factorial

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a number: "))
result = fact(n)
print(result)

# Prac_2a
#vowel

def vowel(s):
    return s.lower() in ['a', 'e', 'i', 'o', 'u']

s = input("Enter a Character: ")
result = vowel(s)
print(result)

# Prac_2b
#length of a given list or string

def findlen(str_or_list):
    counter = 0
    for _ in str_or_list:
        counter += 1
    return counter

str_or_list = input("Enter a string or list: ")
print(findlen(str_or_list))

# Prac_2c
#histofram

def histogram(lst):
    for i in lst:
        print(i * '*')

lst = []
ln = int(input("Enter the list length: "))
print("Enter integer values")
for i in range(ln):
    data = int(input())
    lst.append(data)
histogram(lst)

# Prac_3a
#Pangram

def pangram(str, alphabet):
    flag = True
    for char in alphabet:
        if char not in str.lower():
            flag = False
    if flag:
        print("Pangram")
    else:
        print("Not a Pangram")

str = "The quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"
pangram(str, alphabet)

# Prac_3b
# write a program that prints out all the element of the list that are less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

lst = [i for i in a if i < 5]
print(lst)

# Prac_4a
# atleast one common member

lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 6, 7, 8, 9]
for x in lst1:
    for y in lst2:
        if x == y:
            print("True")

# Prac_4b
# specified after removing the 0th,2nd,4th,5th element

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print("Original List:", lst)
for i in lst:
    if i not in (0, 2, 4, 5):
        print(i, end=" ")

# Prac_4c
#clone or copy a list

original_list1 = [1, 2, 3, 4, 5]
print("Original List1:", original_list1)
new_list = list(original_list1)
print("New List:", new_list)

original_list2 = [6, 7, 8, 9, 10]
print("Original List2:", original_list2)
copy = original_list2.copy()
print("COPY:", copy)

# Prac_5a
# sort a dictionary by value

import operator
d = {'C': 90, 'C++': 100, 'Python': 80, 'Java': 60}
print("Original dictionary:", d)

asc = dict(sorted(d.items(), key=operator.itemgetter(1)))
print("Ascending:", asc)

desc = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print("Descending:", desc)

# Prac_5b
# script to concatenate ,dictionarie to create a new one

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

dict4 = {}
for d in (dict1, dict2, dict3):
    dict4.update(d)
print(dict4)

# Prac_5c
# sum all the items in dictionary

dict1 = {'Python': 90, 'C++': 100, 'Java': 80, 'C': 50}
print(sum(dict1.values()))

dict2 = {'Python': 90, 'C++': 100, 'Java': 80, 'C': 50}
total_sum = 0
for value in dict2.values():
    total_sum += value
print(total_sum)

# Prac_6a
# read an entire text value

f = open("myfile.txt", "r")
print(f.read())
f.close()

# Prac_6b
# to append text a file and display the text

f = open("myfile.txt", "a")
f.write("Eleven")
f.close()

# Prac_6c
# read last N lines

n = int(input("Enter n lines: "))
f = open("myfile.txt", "r")
for line in (f.readlines()[-n:]):
    print(line, end="")
f.close()

# Prac_7a
# information of student and display

class Student:
    def __init__(self, rollno, name, age, phone):
        self.rollno = rollno
        self.name = name
        self.age = age
        self.phone = phone

    def display(self):
        print("Student Roll No =", self.rollno)
        print("Student Name =", self.name)
        print("Student Age =", self.age)
        print("Student Phone Number =", self.phone)

print("----------- Enter Student Details -------------")
rollno = int(input("Enter your roll no: "))
name = input("Enter your name: ")
age = int(input("Enter your age: "))
phone = int(input("Enter your phone: "))

ob = Student(rollno, name, age, phone)
print("--------- Display Student Details ----------")
ob.display()

# Prac_7b
# Inheritance(single,multiple,multi level )

class Parent:
    def first(self):
        print("This is a parent class")

class Child(Parent):
    def second(self):
        print("This is a child class")

ob = Child()
ob.first()
ob.second()

# Multiple Inheritance
class Parent1:
    def fun1(self):
        print("This is Parent1 class")

class Parent2:
    def fun2(self):
        print("This is Parent2 class")

class Child(Parent1, Parent2):
    def fun3(self):
        print("This is Child class")

ob = Child()
ob.fun1()
ob.fun2()
ob.fun3()

# Multi-level Inheritance
class Parent:
    def fun1(self):
        print("This is Parent class")

class Child1(Parent):
    def fun2(self):
        print("This is Child1 class")

class Child2(Child1):
    def fun3(self):
        print("This is Child2 class")

ob = Child2()
ob.fun1()
ob.fun2()
ob.fun3()

# Prac_7c
# dont do
class Numbers:
    MULTIPLER = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return cls.MULTIPLER * a

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    @value.setter
    def value(self, t):
        self.x = t[0]
        self.y = t[1]

    @value.deleter
    def value(self):
        self.x = None
        self.y = None

ob = Numbers(10, 20)
print("Add:", ob.add())
print("Multiply:", Numbers.multiply(10))
print("Subtract:", Numbers.subtract(20, 10))

ob.value = (100, 200)
print("Add:", ob.add())

del ob.value
print("Values:", ob.value)

#pra 8 a
#Try to configure the widget with various options like: bg=â redâ , 

from tkinter import *

window = Tk()
window.title("9a")
window.geometry("300x300")

my_label = Label(
    window, 
    text="Python", 
    bg="red", 
    fg="white", 
    font=('times', 18), 
    width=20
)
my_label.pack()

window.main.loop()


# Prac_8b
#  Try to change the widget type and configuration options to experiment with 
# other widget types like Message, Button, Entry, Checkbutton, Radiobutton, Scale 
# etc.

from tkinter import *

window = Tk()
window.title("9b")
window.geometry("500x500")

my_message = Message(window, text="Registration Form", relief=RAISED, width=150)
my_message.pack(pady=10)

L1 = Label(window, text="Full name ")
L1.pack()
E1 = Entry(window, bd=5)
E1.pack()

L1 = Label(window, text="Email ")
L1.pack()
E1 = Entry(window, bd=5)
E1.pack()

L1 = Label(window, text="Password ")
L1.pack()
E1 = Entry(window, bd=5)
E1.pack()

Button1 = Checkbutton(window, text="Remember", onvalue=1, offvalue=0)
Button1.pack()

Button2 = Checkbutton(window, text="Not Remember", onvalue=1, offvalue=0)
Button2.pack()

R1 = Radiobutton(window, text="Male", value=1)
R1.pack()
R2 = Radiobutton(window, text="Female", value=2)
R2.pack()

my_button = Button(window, text="submit")
my_button.pack(pady=20)

def sel():
    selection = "Value " + str(var.get())
    label.config(text=selection)

var = DoubleVar()
scale = Scale(window, variable=var)
scale.pack()

Button = Button(window, text="Get scale value", command=sel)
Button.pack()

label = Label(window)
label.pack()

window.mainloop()

