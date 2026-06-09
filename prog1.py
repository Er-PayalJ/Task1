file1=open("pattern1.txt","w")
file1.write("hello python\n")
for i in range(1,4+1):
    a="*" *i
    print(a)
    file1.write(a + "\n")

print()