file1=open("pattern5.txt","w")
file1.write("hello python\n")

for i in range(1,4+1):
    for j in range(1,4+1):
        print("#",end=" ")
        file1.write("# ")
    print()
    file1.write("\n")
print()