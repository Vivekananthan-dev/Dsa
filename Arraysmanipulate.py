#By default we cant create array in python we use list instead if want use numpy

l =[1,2,3,4]
print("list: ", l)
print("list[3]: ",l[3])

print("list[]: ",l[-2])

print("for loop: ")
for i in range(len(l)):
    print("index [",i,"] :",l[i]) # print(f"index[{i}]: {l[i]}"

print("for each: ")
for i in l:
    print(i)