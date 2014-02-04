#!/usr/bin/env python

def welcome():
    print "Welcome to Snayer's Temperature Scale Converter"
    print "Enter the number of the temperature you have"
    question()

def question():
    print "\t1. Celsius"
    print "\t2. Fahrenheit"
    print "\t3. Kelvin\n"
    choice = raw_input("> ")
    if choice == "1":
        Celsius()
    elif choice == "2":
        Fahrenheit()
    elif choice == "3":
        Kelvin()
    else:
        print "Please enter 1, 2, or 3 to convert your temperature to other forms."
        question()

def Celsius():
    print "Please enter your temperature"
    cels = float(raw_input("> "))
    fahr = 9.0/5.0 * cels + 32
    print cels, " degrees in Fahrenheit is ", fahr
    kelv = cels + 273.15
    print cels, " degrees in Kelvin is", kelv
    repeat()

def Fahrenheit():
    print "Please enter your temperature"
    fahr = float(raw_input("> "))
    cels = (fahr - 32) * 5.0/9.0
    print fahr, " degrees in Celsius is ", cels
    kelv = cels + 273.15
    print fahr, " degrees in Kelvin is ", kelv
    repeat()

def Kelvin():
    print "Please enter your temperature"
    kelv = float(raw_input("> "))
    cels = kelv - 273.15
    print kelv, " degrees in Celsius is ", cels
    repeat()
 
def repeat():
    print "Do you have more conversions? (y or n)"
    choice = raw_input("> ")
    if choice == "y":
        question()
    else:
        exit

welcome()