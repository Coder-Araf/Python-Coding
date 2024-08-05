# age = int(input("Enter Your Age : "))
#
# if (age > 18):
#     print("You can Vote.")
# elif(age >= 16):
#     print("You are in Registered")
# else:
#     print("You Cannot Vote.")
#
# print("End")

#College Statement
mark = int(input("Enter Your Mark: "))

if(mark >= 80):
    if(mark > 100):
        print("Can't Find")
    else:
        print("A+")
elif(mark >= 70):
    print("A")
elif(mark >= 60):
    print("A-")
elif(mark >= 50):
    print("B")
elif(mark >=33):
    print("C")
else:
    print("Fail")



num = int(input("Enter your number: "))

if(num%2==0):
    print("Even")
else:
    print("Odd")