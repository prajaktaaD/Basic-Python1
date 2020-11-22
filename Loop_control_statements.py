x=int(input("enter the num of items:"))
i=1
stock=7
while(i<=x):
    if(i<=stock):
        print("issue product=",i)
        i+=1
        continue
    else:
        print("out of stock")
        i=i+1
        break
