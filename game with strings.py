import random
words={1:'antidodes',2:'ball',3:'coconut',4:'daughter',5:'whiteelephant',6:'fisherman',7:'googledocs',8:'higherclasees',9:'iscontemple',10:'jockey',11:'kingfisher',12:'lightrace',13:'manganese',14:'nightout',15:'output',16:'pedestrians',17:'quotient',18:'rhinosorous',19:'stifunds',20:'travelling',21:'uranus',22:'ventilation',23:'wildwolf',24:'xray',25:'yolk',26:'zebra'}
w=random.randint(1,26)
n=str(input("Enter your name"))
a=words[w]
print("guess the word that is  a ",len(words[w]),"word")
number=1
chance=0
won=0
b='_'*len(a)
print("Enter an alphabet so that i will tell u does my word contain alphabet and if it contains i will be telling you at what place its is present ")
while(chance<6 and won!=1):
    count=0
    d=str(input("Enter an alphabet"))
    for i in range(0,len(a)):
        c=ord(a[i])
        if(c==ord(d)):
            count+=1;
    print(d,' count is ',count)
    if count >=1:
        b=b[:a.index(d)] + d + b[a.index(d) + 1:]
        print(' '.join(b))
    if(number>2):
        userans=str(input("Guess the word now!!!!!!!!!!!"))
        if(userans==a):
            print("Hurry you won the game !!!!")
            won=1
        else:
            print("you lost the chance!!!")
    chance+=1
    number+=1
if(won!=1):
    print("oops ",n,"you are made fooled by yaswanth's word and yaswanth's word is ",a) 
           
