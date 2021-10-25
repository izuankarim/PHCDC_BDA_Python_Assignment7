#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
D15P1. F2C Conversion
Write a program that takes as input Fahrenheit temperature. It converts the input temperature to Celsius and prints out the converted temperature as shown in the example. The formula for conversion between the two is: C=5/9(F−32), Where C is the temperature in Celsius and F is the temperature in Fahrenheit.
NOTE:
1.	DO NOT use any prompts in the input().
2.	Use the round() function to round your answer to up to two decimal places. That is, use round(VALUE, 2).
"""

F=float(input("Temperature in Farenheit: "))
C=(5/9)*(F-32)

print("Farenheit temperature",F," is the same as " ,round(C,2),"degrees Celsius")


# In[2]:


"""
D15P2. Final Velocity
Write a program that takes as input three numbers, u, a, and t. Here u stands for the initial velocity, a 
stands for the acceleration, and t stands for the time duration. The program prints the final velocity (v).

The input will consist of three lines. The first line will contain the initial velocity u, the second line 
will contain acceleration a and the third line will contain time t. Recall that u and a can take any real (float) 
values as velocity and acceleration are continuous vector quantities (in physics). Time t can take non-negative 
real values only, i.e., 0 ≤ t.
 
NOTE:
1.	DO NOT use any prompts in the input().
2.	The formula for computing the final velocity: v=u+at
3.	Use the round() function to round a VALUE to up to two decimal places:  round(VALUE, 2)
"""

u=float(input("Initial speed:"))
a=float(input("Acceleration:"))
t=float(input("Time:"))
v=u+(a*t)
print("The Final Velocity is", round(v,2))


# In[4]:


"""
D15P3. Displacement Covered
Write a program that takes as input three numbers, u, a, and t. Here u stands for the initial velocity, 
a stands for the acceleration, and t stands for the time duration. The program prints the displacement covered (d) 
in time t.

The input will consist of three lines. The first line will contain the initial velocity u, the second line will 
contain acceleration a and the third line will contain the time t. Recall that u and a can take any real value as 
velocity and acceleration are continuous vectors (in physics). Time t can take non-negative real 
values only, i.e., 0 ≤ t.

NOTE:
1.	DO NOT use any prompts in the input().
2.	The formula for computing the displacement:  d=ut+1/2at2
3.	Use the round() function to round a VALUE to up to two decimal places:  round(VALUE, 2).
"""

u=float(input("Initial speed:"))
a=float(input("Acceleration:"))
t=float(input("Time:"))
d=(u*t)+((a*t*t))/2
print("The Displacement is", round(d,2))


# In[6]:


"""
D15P4. Number of Days
Write a program that takes as input an Integer s, the number of seconds elapsed for a certain event. The program 
converts s to hours (hh), minutes (mm), and seconds (ss) and prints the output as hh:mm:ss.
- Convert seconds in hour, minute and seconds

Note that the input will only be positive integer values since time cannot be negative.
"""

s=int(input("Duration in second(s): "))
if s>=0:
    h = round(s // 3600)
    m = round((s-(3600*h)) // 60)
    s = round(s- (3600*h)-(m*60))
    print(h,":",m,":",s)
else:
    print("Input will only be positive integer values since time cannot be negative. Please try again.")


# In[8]:


"""
D15P5. Leap Year
Write a program to check if the given year is a leap year or not.
The program should read an integer (year) from a user. Display the Boolean value: True if the year is a 
leap year, False if not.
"""

def CheckLeap(Year):

# Check if the given year is a leap year
    if ((Year % 400 == 0) or
    (Year % 100 != 0) and
    (Year % 4 == 0)):
        print("True");
        
# If not a leap year
    else:
        print("False")
        
Year=int(input("Please Enter the Year Number:"))
CheckLeap(Year)


# In[17]:


"""
D15P6. Reverse the number
Write a program to find reverse of the number.
The program should read an integer (number) from a user. The program should print the reverse of the given input.
"""

num = int(input("Please enter the number:"))
print (str(num)[::-1])
print (type(num))


# In[22]:


"""
D15P7. Display Multiplication table
Write a program to Display the multiplication table.
The program should read an integer (Multiplier and Range) from a user. The program should print the 
multiplication table for following format.

Input: 4   10

Output
1*4=4
2*4=8
3*4=12
…
10*4=40

"""
num = int(input("Multiplier: "))
upto = int(input("Up until range, i.e. 1-12: "))


# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, upto+1):
   print(num, 'x', i, '=', num*i)


# In[25]:


"""
D15P8. Prime number Checking
Write a program to check whether given number is prime or not.
The program should read an integer (number) from a user. The program should print the number is prime or not.
"""


# To take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

#if input number is less than or equal to 1, it is not prime

else:
   print(num,"is not a prime number")

