#For loop= execute a block of code a fixed number of times.
# you can iterate over a range, string sequence, etc.


for i in range(1, 11): #range() function is used to generate a sequence of numbers, it takes three parameters: start, stop, and step.
    print("Hello")

print("Done")

for i in (reversed(range(1, 11))): #reversed() function is used to reverse the order of the range
    print("Hello")

print("Done")

for i in range(1, 11, 2): #step parameter is used to specify the increment between each number in the range. here 2 acts as a step size.
    print(i)

print("Done")
