import random
c_num=random.randrange(1,201)
user_input=int(input("Enter your number:"))
if user_input>c_num:
    print("computer number",c_num)
    print("Your Guess Number is Too High")
elif c_num>user_input:
    print("computer number",c_num)
    print("Your Guess Number is Too Low")
else:
    print("computer number",c_num)
    print("Your Guess number is Equal")

