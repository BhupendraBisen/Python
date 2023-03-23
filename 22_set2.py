# s1 = {1,2,5,7}
# s2 = {3,6,7}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities2 = {"Tokyo","seoul","kabul","Madrid"}
# # cities3 = cities.union(cities2)
# cities.intersection_update(cities2)
# print(cities)

# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities2 = {"Tokyo","seoul","kabul","Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities2 = {"Tokyo","seoul","kabul","Madrid"}
# cities3 = cities.difference(cities2)
# print(cities3)

# cities = {"Tokyo2","Madrid","Berlin","Delhi"}
# cities2 = {"Tokyo","seoul","kabul","Madrid2"}
# cities3 = cities.isdisjoint(cities2)
# print(cities3)

# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities2 = {"seoul","kabul",}
# # print(cities.issuperset(cities2))
# cities3 = {"Tokyo", "Madrid"}
# # print(cities.issuperset(cities3))
# print(cities3.issubset(cities))

# cities = {"Tokyo","Madrid","Berlin", "delhi"}
# cities.add("india")
# cities.remove("Tokyo")
# cities.discard("Tokyo2")
# print(cities)

# cities = {"Tokyo","Madrid","Berlin", "delhi"}
# print(cities.pop())
# cities.discard("Tokyo2")
# print(cities)

# cities = {"Tokyo","Madrid","Berlin", "delhi"}
# del cities
# print(cities)

info = {"carlo", 56,78,89,98,3,True}
if "carlo" in info:
    print("carlo is present")
else:
    print("carlo is absent")
