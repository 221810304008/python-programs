import random
b=random.randint(1,100)
n=str(input('enter your name'))
f=0
for i in range(5):
    if f!=1 :
        a=(int(input("enter the number")))
        if a==b:
            print('Won the game',b)
            f=1
        elif a > b :
            print(a,' greater than expected number')
        elif a < b :
            print(a,' less than expected number')
        
if f==0 :
    print(' oops!!!! ',n,'! Better luck next time!!!!!!!','\n','You were made fool by Yaswanth','\n','Yaswanth number is',b)  





             
