# Check for True
# Check for False

#  Non-Zero and Non-Null values are True
#  Zero and Null are False

'''
if condition:
    # block of codes
'''

# num = -5
# if num > 0:
#     print ("Positive Number")
#     print ("Another statement...")
# print ("Continue with program code ...")


'''
if condition:
    #block of codes if the condition is True
else:
    #block of codes if the condition is False
'''
# num = -3
# if num >= 0:
#     print ("Number is positive ")
# else:
#     print ("Number is negative ")

'''
if condition1:
    #block1
elif condition2:
    #block2
elif condition3:
    #block3
else:
    #block4
'''

# num = -1
# if num > 0:
#     print ("positive number ")
# elif num==0:
#     print ("zero")
# else:
#     print ("negative number")

'''
Nested If statements

if condition1:
    if condition2:
        #block of code
    else:
        #block of code
elif conditionX:
    #block of code
else:
    #block of code
'''

# num = -3
# if num >= 0:
#     if num == 0:
#         print ("Zero")
#     else:
#         print ("Positive number")
# else:
#     print ("Negative number")


'''
passing grade >= 75
    grade >= 90
        Award : with high honor
    grade >=85
        Award : with honors
    else
        Passed with no honors
else
    Failed

'''

# grade = int(input("Enter your grade from 0-100: "))
# if grade >= 75:
#     print ("Status: Passed")
#     if grade >= 90:
#         print ("Award with high honor ")
#     elif grade >=85:
#         print ("Award with honors ")
#     else:
#         print ("No Award")
# else:
#     print ("Status: Failed ")


'''
Single Line if statement

if condition:action
'''

# a = 10
# b = 5
# if a>b:print ("a is greater than b")

'''
Loops

While loop

while condition:
    #block of codes

'''

# count = 0       #init
# while count < 5:    #condition
#     print ("Counter ",count) #Body execute if true
#     count += 1 #counter (inc)
# print ("End of Code..")

'''
while loop with else
'''
# count = 0
# while count < 5:
#     print ("Inside Loop ",count)
#     count += 1  # 5 < 5
# else:
#     print ("Loop Finished!")
# print ("End of code...")

'''
Iterating over a list
for variable in sequence:
    #execute code block
'''
# fruits = ["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)

'''
Iterating over a string
'''
# message = "Hello World"
# for char in message:
#     print (char)

#range()

# for i in range(5): #Generate numbers form 0 to 4
#     print (i)

#Start / Stop
# for i in range(1,6):
#     print (i)

#range - Start, Stop and Step
# for i in range(1,12,2): #Generate numbers from 0-9 
#     print (i)

#negative Steps
# for i in range(10,0,-1):
#     print(i)

'''
Iterating over a list
'''
# fruits = ["apple","banana","cherry"]
# for i in range(len(fruits)):
#     print (f"Index {i}: {fruits[i]}")

'''
using range with condition statement

'''
# for i in range(1,11): 
#     if i % 3 == 0:
#         continue
#     print(i)

# if True:
#     pass
# print ("This is after pass")

#nested loop with range

# for i in range(3):
#     for j in range(3):
#         print (f"{i}, {j}",end=' ')
#     print()

#range with break
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)

#range with else 

# for i in range (1,11):
#     if i==11:
#         break
#     print(i)
# else:
#     print ("Loop Completed")

#create multiplication table
#5x5 

# for i in range(1,6):
#     for j in range(1,6):
#         print (f"{i} x {j} = {i} * {j}",end='\n')
#     print() #move to the next line 