#Read file
f1 = open("SampleFile.txt","r")
print(f1.readline())

for data in f1:
    print(data)


# write the file
# f2 = open("myfile","w")
#
# f2.write("something")

f3 = open("myfile","a")
f3.write("something 2")