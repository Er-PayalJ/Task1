file1=open("pattern6.txt","w")
file1.write("hello python \n")
a=1
for i in range(1,4+1):
    for j in range(i):
        print(a,end=" ")
        file1.write(str(a) +" ")
        a=a+1
    print()
    file1.write("\n")
print()