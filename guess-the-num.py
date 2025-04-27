import random
rand_num = random.randint(1,100)
max_attempts = 3
attempts = 0
print(rand_num)
try:
    user_num = int(input('Guess a number between the range 1-100 :'))
except ValueError:
    print("Enter an integer, genius!")
while user_num != rand_num and attempts < max_attempts:
    attempts += 1
    diff = abs(rand_num - user_num)
    if diff<=10:
        print("You were extremely close to the number!")
    elif diff<=30:
        print("You were pretty close to the number!")
    elif diff<=50:
        if diff>rand_num:
            print("Your guess is higher than the number!")
        else:
            print("Your guess is too low!")
    else:
        if user_num > rand_num:
            print("You're way too high!")
        else:
            print("You're way too low!")
    if attempts < max_attempts:
        print(f"{attempts} out of {max_attempts} done!")
        user_num = int(input("Try Again :"))

if user_num==rand_num:    
    print('BINGO! Your guess was correct!')
else:
    print(f"{rand_num} was the correct number! \nBetter Luck Next Time!")