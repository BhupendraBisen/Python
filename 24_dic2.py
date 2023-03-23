ep1 = {122:45, 123:89, 567:79, 690:79}
ep2 = {222: 67, 566:90}
# ep1.update(ep2)
# print(ep1)
# ep1.clear()
# ep1.pop(567)
ep1.popitem()
print(ep1)
del ep1[122]
print(ep1)