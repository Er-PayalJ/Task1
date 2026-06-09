file1=open("pattern3.txt","w")
file1.write("hello python \n")
for i in range(1,4+1):
    a="" 
    for j in range(1,i+1):
        a= a+str(j)+""
    print(a)
    file1.write(a + "\n")

print()