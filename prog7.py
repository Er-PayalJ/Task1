file1=open("pattern1.txt","w")
file1.write("hello python\n")
for i in range(1,4+1):
    a="*" *i
    print(a)
    file1.write(a + "\n")
print("---------------------")


file1=open("pattern2.txt","w")
file1.write("hello python\n")
for i in range(4,-1,-1):
    a="*" *i
    print(a)
    file1.write(a + "\n")
print("---------------------------")


file1=open("pattern3.txt","w")
file1.write("hello python \n")
for i in range(1,4+1):
    a="" 
    for j in range(1,i+1):
        a= a+str(j)+""
    print(a)
    file1.write(a + "\n")
print("-----------------------------")


file1=open("pattern4.txt","w")
file1.write("hello python\n")
for i in range(1,4+1):
    a=str(i) *i
    print(a)
    file1.write(a + "\n")
print("-----------------------------")


file1=open("pattern5.txt","w")
file1.write("hello python\n")

for i in range(1,4+1):
    for j in range(1,4+1):
        print("#",end=" ")
        file1.write("# ")
    print()
    file1.write("\n")
print("-----------------------------")


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