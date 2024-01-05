#Task -5
import random

char="abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*_+"

while(1):
    length=int(input("Enter the length of password : "))
    password= ""
    
    for i in range(length):
        password+= random.choice(char)
    print("\n ","Strong Password: "+password,"\n")
    flag=int(input("Do You want to generate again Password : "))
    if flag==0:
        break;