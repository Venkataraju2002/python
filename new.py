s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())
s6=int(input())
score=s1+s2+s3+s4+s5+s6
per=(score/600)*100



if s1>=35:
    if s1>=75:
        print("english:",s1 ,"/100", "p","/A+")
    elif s1>=65:
        print("english:",s1 ,"100",  "p","/A")
    elif s1>=55:
        print("english:",s1 ,"100",  "p","/B")
    elif s1>=35:
        print("english:",s1 ,"100",   "p","C")
else:
    print("english:",s1 ,"100",   "f","f")
if s2>=35:
    if s2>=75:
        print("telugu:",s2 ,"100",  "p","/A*")
    elif s2>=65:
        print("telugu:",s2 ,"100",  "p","/A")
    elif s2>=55:
        print("telugu:",s2 ,"100",  "p","/B")
    elif s2>=45:
        print("telugu:",s2 ,"100",   "p","C")
else:
    print("telugu:",s2 ,"100",   "f","f")

if s3>=35:
    if s3>=75:
         print("hindi:",s3 ,"100", "p","A+")
    elif s3>=65:
        print("hindi:",s3 ,"100",  "p","A")
    elif s3>=55:
        print("hindi:",s3 ,"100",  "p","B")
    elif s3>=35:
        print("hindi:",s3 ,"100",   "p","C")
else:
    print("hindi:",s3 ,"100",   "f","f")
if s4>=35:

    if s4>=75:
        print("maths:",s4 ,"100", "p","A+")
    elif s4>=65:
        print("maths:",s4 ,"100",  "p","A")
    elif s4>=55:
        print("maths:",s4 ,"100",  "p","B")
    elif s4>=35:
        print("maths:",s4 ,"100",   "p","C")
else:
     print("maths:",s4 ,"100",   "f","f")
if s5>=35:
    if s5>=75:
        print("science:",s5 ,"100", "p","A+")
    elif s5>=65:
        print("science:",s5 ,"100",  "p","A")
    elif s5>=55:
        print("science:",s5 ,"100",  "p","B")
    elif s5>=35:
        print("science:",s5 ,"100",   "p","C")
else:
    print("science:",s5 ,"100",   "f","f")
if s6>=35:
     if s6>=75:
          print("social:",s6 ,"100", "p","A+")
     elif s6>=65:
          print("social:",s6 ,"100",  "p","A")
     elif s6>=55:
          print("social:",s6 ,"100",  "p","B")
     elif s6>=35:
          print("social:",s6 ,"100",   "p","C")
else:
     print("social:",s6 ,"100",   "f","f")
print("marks:",score)
print("percent:",per)
if (s1<=35 and s2<=35 and s3<=35 and s4<=35 and s5<=35 and s6<=35):
    per = 0
    if((s1 and s2 and s3 and s4 and s5 and s6)>=35):
        if per>=75:
            print("Overal percentage:",per,"/100","p","Grade: A+")
        elif per>=65:
            print("Overal percentage:",per,"/100","p","Grade: A")
        elif per>=55:
            print("Overal percentage:",per,"/100","p","Grade: B")
        elif per>=35:
            print("Overal percentage:",per,"/100","p","Grade: C")
else:
    print("Overal percentage:",per,"/100","f","Grade: Fail")
