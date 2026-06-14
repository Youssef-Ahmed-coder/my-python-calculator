num1 = float(input("enter frist number\n"   ))
chose = str(input(" chose / * + -   \n"))
num2 = float(input("enter frist number   \n"))
result2 = ""
def give_resalt(resalt):
    print (num1,chose,num2,"= ",resalt)
if chose == "+" :
    resalt2 = num1 + num2
    give_resalt(resalt2)

elif chose == "-" :
    resalt2 = num1 - num2
    give_resalt(resalt2)   

elif chose == "*" :
    resalt2 = num1 * num2
    give_resalt(resalt2) 
    
elif chose == "/" :
    if num2 == 0:
        print("MATH ERROR!!!\n")
    else :
        resalt2 = num1 / num2
        give_resalt(resalt2)    
else:
    print ("you don't chose")