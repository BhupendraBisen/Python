# def average(a,b):
#     print ("The average is",(a+b)/2)

# average(7,9)

# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)
# name("Amy")

def average(*numbers):
    sum =0
    for i in numbers:
        sum = sum+i
    # print("Average is:",sum / len(numbers))
    # return 4
    return sum / len(numbers)
c= average(9,8,6,4,3)
print(c)
# def name(**name):
#     print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])
#
# name(mname = "Buchanan", lname = "Barnes", fname = "James")
