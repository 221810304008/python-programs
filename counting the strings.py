a=(input("enter the string"))
b=(input("enter the string to get its count"))
count=0;
for x in range(0,len(a)):
    c=ord(a[x])
    if(c==ord(b)):
        count=count+1;
print(count)
