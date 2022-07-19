#find factorial of the number without function

num = int(input("enter the number : "))
f = 1
if num<0:
    print("does't exit nagative value")
else:
    for i in range(1,num+1):
        f = f*i
    print("fACTORIAL IS ",num ,"is",f)    
