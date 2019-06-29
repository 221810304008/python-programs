# Take random inputs
# if equal print "Equal"
# Else print whether the given number is "greater" or "lesser"
# Ex. b=5 ; a=25 ; a > b
# Ex. b=5 ; a=2  ; a < b
# Ex. b=5 ; a=7  ; a > b
# Ex. b=5 ; a=10 ; a > b
# Ex. b=5 ; a=5  ; a = b  " Won the game"
import random
def prime(): 
    flag=0
    while(flag==0):
        n=random.randint(1,250)
        count=0
        for i in range(2,n+1):
            if(n%i==0):
                count+=2
        if(count==2):
            flag=1
            return n
print("WELCOME TO yvshu's WORLD!!!")
b=prime()
n=str(input('enter your name'))
f=0
c=6
for i in range(6):
    if f!=1 :
        a=(int(input("enter the number")))
        if a==b:
            print('Won the game',b)
            f=1
        elif a > b:
            print(a,'is greater than expected number')
            c-=1
            if(c<2):
                print("You r left with 1 chances only!!! GET READY TO LOSE THE GAME :)")
        elif a < b:
            print(a,'is less than expected number')
            c-=1
            if(c<2):
                print("You r left with 1 chances only!!! GET READY TO LOSE THE GAME :)")
        
        
if f==0 :
    print(' oops!!!! ',n,'! Better luck next time!!!!!!!','\n','You were made fool by Yaswanth','\n','Yaswanth number is',b)  


             







