# #For loop= execute a block of code a fixed number of times.
# # you can iterate over a range, string sequence, etc.


# for i in range(1, 11): #range() function is used to generate a sequence of numbers, it takes three parameters: start, stop, and step.
#     print("Hello")

# print("Done")

# for i in (reversed(range(1, 11))): #reversed() function is used to reverse the order of the range
#     print("Hello")

# print("Done")

# for i in range(1, 11, 2): #step parameter is used to specify the increment between each number in the range. here 2 acts as a step size.
#     print(i)

# print("Done")

# #EX 1:
# credit_card= "1234 5678 9012 3456"

# for i in credit_card:
#     print(i)
# print("Done")

# for i in credit_card[1:17]: #here we are slicing the string to get the characters from index 1 to 16 (17 is exclusive)
#     print(i)
# print("Done")

# for i in credit_card[1:17:2]: #step parameter is used to specify the increment between each number in the range. here 2 acts as a step size.
#     print(i)
# print("Done")

# # Ex 2

# for i in range(1, 21):
#     if i == 13:
#         continue #continue statement is used to skip the current iteration of the loop and move to the next iteration.
#     else:
#         print(i)
# print("done")

# for i in range(1, 21):
#     if i == 13:
#         break #break statement is used to exit the loop prematurely when a certain condition is met. In this case, when i equals 13, the loop will terminate and the program will continue with the next line of code after the loop.
#     else:
#         print(i)
# print("done")

# #While loop: execute some code while some condition remains true.

# name= input("Enter your name")
  
# while name == "":
#     print("You did not enter your name")
#     name = input("ENter your name: ")

# print(f" Hello {name}")

#Ex 2:
# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age=int(input("Enter your age: "))

# print(f"you are {age} years old")

food = input("Enter a food you like (q to QUIT):")

while not food == "q":
    print(f"you like {food}")
    food = input("enter another food you like (q to QUIT): ")

print("BYE")