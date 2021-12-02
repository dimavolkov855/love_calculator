print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
both_names = name1 + " "+ name2

both_names.count('t')
both_names.count('r')
both_names.count('u')
both_names.count('e')

s_true= both_names.count('t') + both_names.count('r') + both_names.count('u') + both_names.count('e')

both_names.count('l')
both_names.count('o')
both_names.count('v')
both_names.count('e')

s_love = both_names.count('l') + both_names.count('o') + both_names.count('v') + both_names.count('e')

score = str(s_true) + str(s_love)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) >= 40 and int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


