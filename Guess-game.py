import random
num = random.randint(0, 9)
secret_no = num
no_of_trial = 1
while no_of_trial <= 5:
    print('Guess a lucky digit')
    while True:
        try:
            p = int(input('>>'))
        except ValueError:
            print("This is an unaccepted response, enter a valid integer value")
            continue
        else:
            break
    if p > 9:
        print("enter a single digit")
    else:
        if p == int(secret_no):
            print('''
            correct
            YOU WON! 
            ''')
            break
        else:
            print('Incorrect guess')
            x = abs(p-secret_no)
            if 3 < x < 7:
                print('Not very close')
            elif 0 < x < 4:
                print('you are close mate')
            else:
                print('you are far from the number')
            if no_of_trial < 5:
                print(f'''
                try again
                no of trials left = { 5 - no_of_trial }
                ''')
            no_of_trial += 1
else:
    print('YOU LOSE!')
print('secret number is ' + str(secret_no))
print('THE END')

