from msilib import datasizemask
import random
data={
    "3456781234":{
        "name": "desmond",
        "dob":  "09-09-09",
        "bvn":  "123456237865473",
        "pin":  "3412",
        "bal":  30000
    }   
}

print("welcome to the AstroBank app")
print("enter s to signup l to login:")
choice=input(">").lower()

if choice=='l':
    acc_num=input ("enter your account number:\n>")
    pin=input("enter your pin:\n>")

    user=data.get(acc_num)
    
    if user is not None and user["pin"]==pin:
        print("success")
        print(f"welcome {user['name']}.\nYour account balance is #{user['bal']}")
        
        print("""\nwhat would you like to do?
        press 1 to withdraw
        press 2 to deposit
        press any other key to quit.""")

        user_input=input(">")

        if user_input=="1":
            amount=int(input("how much?\n"))
            if amount>=user["bal"]:
                print("insufficient funds")
            else:
                user["bal"]-=amount
                print("please take your cash")
                print(f"balance is {user['bal']}")
        elif user_input=="2":
            amount=int(input("how much\n>"))
            user["bal"]+=amount
            print("successfully deposited")
            print(f"your new balance is {user['bal']}")

    
    else:
        print("invalid login")
elif choice=="s":
    name=input("welcome\n please enter your full name\n>")
    dob=input("enter your date of birth in this format ddmmyy\n> ")
    bvn=input("please enter your bvn\n>")
    pin=input("create your four digit code\n>")
    details=[("name", name),
             ("dob", dob),
             ("bvn", bvn),
             ("pin", pin),
             ("bal", 0)
            ]
    num=[1,2,3,4,5,6,7,8,9,0]
    acc_num_list=[str(random.choice(num))for _ in range(10)]

    accountnumber="".join(acc_num_list)

    data[accountnumber]=dict(details)
else:
    print("invalid input")

    




    


