def add(n1,n2):
    return n1+n2
    
def sub(n1,n2):
    return n1-n2
    
def mul(n1,n2):
    return n1*n2
    
def div(n1,n2):
    return n1/n2
    

#-----------input num
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

choice=int(input("enter choice \n1-sum\n2-sub\n3-mul\n4-div:"))

#----------function call
if(choice==1):
    print("sum=",add(num1,num2))
    
if(choice==2):
   print("sub=",sub(num1,num2))
   
if(choice==3):
    print("mul=",mul(num1,num2))    

if(choice==4):
    print("div=",div(num1,num2))
