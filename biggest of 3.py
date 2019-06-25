a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
if(a>b and a>c):
    print("a is big");
elif(b>a and b>c):
    print("b is big");
elif(c>a and c>b):
    print("c is big");
else:
    print("all are equal");
