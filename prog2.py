file1=open("pattern2.txt","w")
file1.write("hello python\n")
for i in range(4,-1,-1):
    a="*" *i
    print(a)
    file1.write(a + "\n")

print()