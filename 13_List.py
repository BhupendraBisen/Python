
# marks = [5,6,4,"bhupendra",True,67,45,34,6,7]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[-3]) # Negative index
# print(marks[len(marks)-3])
# print(marks[5-3]) # positive Index
# print(marks[2]) # positive

# if 7 in marks:
#     print("Yes")
# else:
#     print("No")

# if "bhup" in "bhupendra":
#     print("Yes")

# print(marks)
# print(marks[1:9])
# print(marks[1:9:2])

# lst = [i*i for i in range(10)]
# print(lst)
# lst = [i*i for i in range(10) if i%2]
# print(lst)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)