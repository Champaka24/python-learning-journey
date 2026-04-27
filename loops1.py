# is_failed = True
# i=1

# while is_failed and i<=100:
#     print(f"try {i}")
#     i=i+1
    
# print("Done")


# is_failed = True
# i=1

# while is_failed :
#     print(f"try {i}")
#     i=i+1
#     if i>100:
#         break

# print("Done")

# is_failed = True
# i=1

# while is_failed :
#     if i%2 != 0:
#         i=i+1
#         continue
#     print(f"try {i}")
#     i=i+1
#     if i>100:
#         break

# print("Done")

# i=0

# while i<=10:
#     print(i)
#     i += 1 #i+1

# i=0

# while i<=10:
#     print("*"*i)
#     i += 1 #i+1

# i=1

# while i<=10:
#     x=0
#     while x<i:
#         print("hello", end="-")
#         x =x+1
#     print("")
#     i=i+


pin = "1234"
trails = 1

while trails<=3:
    input_pin=input(f"Trails-{trails} | PIN>>")
    trails += 1
    if input_pin == pin:
        print("Success")
        break
    else:
        print("failed")
    