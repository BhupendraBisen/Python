dic = {
    456: "human being",
    345:  "object",
    786: "bhupendra",
    890: "shikha"
}
# print(dic[890])
# print(dic.get(890))
# print(dic.values())
# print(dic.keys())

# for key in dic.keys():
#     # print(dic[key])
#     print(f"The value corresponding to the key{key} is {dic[key]}")

print(dic.items())
for key,value in dic.items():
    print(f"The value corresponding to the key{key} is {value}")


