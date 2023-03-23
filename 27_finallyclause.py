def func1():
  try:
    l = [1,2,3,4,5,6]
    i = int(input("Enter the index:"))
    print(l[i])
    return 1
  except:
    print("some error occured")
    return 0
  finally:
    print("I am always exucted")

x = func1()
print(x)