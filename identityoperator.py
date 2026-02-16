aa = [2,3,4,5]
bb = [3,4,5,6]
cc = aa 

print("the id of aa is", id(aa))
print("the id of bb is", id(bb))
print("the id of cc is", id(cc))

print(aa is bb)
print(aa is cc)
print(bb is cc)
print(aa is not cc)
print(aa is not bb)
print(bb is not cc)

