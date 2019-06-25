#program for ages
type=input("  Enter  m  for male and  f  for female    ")
print()
age=int(input("Enter your age"))
print()
if(type=='m'):
    if(age>=0 and age<=18):
        print("you are ",age,"yearsold boy")
    elif(age>=19 and age<=30):
        print("you are",age,"years old teenager")
    elif(age>=31 and age<=50):
        print("you are",age,"years old responsible person")
    elif(age>=51 and age<=75):
        print("you are",age,"years old retired grand father ")
    else:
        print("you are",age,"years old ready for death")
else:
    if(age>=0 and age<=18):
        print("you are ",age,"yearsold girl")
    elif(age>=19 and age<=30):
        print("you are",age,"years old teenage girl ")
    elif(age>=31 and age<=50):
        print("you are",age,"years old responsible woman  ")
    elif(age>=51 and age<=75):
        print("you are",age,"years old retired grand mother")
    else:
        print("you are",age,"years old ready for death")
        
