import random as r

def genrate_num():
    number=r.randint(1,100)
    return number

def guess_number(number):
    tries=0
    while True:
        num=int(input("Guess a number between 1 to 100="))
        if num==number:
            print(f"Correct number guess in {tries} tries and the number is {number}")
            break
        elif number>num :
            print("High")
            tries=tries+1
        
        else:
            print("Low")
            tries=tries+1

number=genrate_num()
guess_number(number)
