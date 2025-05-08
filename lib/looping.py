#!/usr/bin/env python3

def happy_new_year():
    x = 10
    while x > 0:
        print(x)
        x-=1
    print("Happy New Year!")
    

def square_integers(int_list):
    return[num**2 for num in int_list]

def fizzbuzz():
    i=1
    while i <= 100:
     if i%3==0 and i%5==0 :
        print ("FizzBuzz")
     elif i % 3== 0:
        print ("Fizz") 
     elif i % 5 == 0:
        print("Buzz")
     else:
        print (i)
     i+=1
print(fizzbuzz())
