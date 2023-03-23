# try :
#     a = 10
#     b = 5
#     out = a/b
#     print (out)
# except:
#     print("denomerator can not be zero")

# import os
# cwd = os.getcwd()
# print("current working directory", cwd)

# cwd = os.F_OK
# print("current working directory",cwd)

# import os
# import sys
# path1 = os.access("factorial.py", os.F_OK)
# print("Exit path",path1)
#
# path2 = os.access("factorial.py",os.R_OK)
# print("It access to read the file:",path2)
#
# path3 = os.access("factorial.py",os.W_OK)
# print("It access to write the file:",path3)
#
# path4 = os.access("factorial.py",os.X_OK)
# print("check if path can be executed", path4)

import calendar
# yy = 2023
# mm = 2
print("calendar of year 2023 is")
print(calendar.calendar(2023))
