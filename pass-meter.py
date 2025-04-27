import re
print("Password must be atleast 8 characters long, containing atleast one uppercase and lowercase letter, one number and one special character.")
password = str(input("Enter Password: "))
score = 0
problem = None
if (len(password))>=8:
    score +=1
else:
    print("Password must be alteast 8 characters long!")
    problem = 1
if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
    score += 1
else: 
    print("The password should contain both uppercase and lowercase letters!")
    problem = 2
if re.search(r"\d", password):
    score += 1
else:
    print("The password should contain atleast one number (0-9).")
    problem = 3
if re.search(r"[!£$%^&*()_\-=+]", password):
    score +=1
else:
    print("The password should contain atleast one special character (!£$%^&*()_-=+).")
    problem = 4

if score == 4:
    print("You have created a strong password.")
elif score ==3:
    if problem == 2:
        print("The passwords strength is intermediate, you can improve the password strength by adding uppercase or lowercase letters.")
    elif problem == 3:
        print("The passwords strength is intermediate, you can improve the password strength by adding numbers.")
    elif problem == 4:
        print("The passwords strength is intermediate, you can improve the password strength by adding atleast one special case characters [!£$%^&*()_-=+].")
elif score == 2:
    print("Weak password, create a strong password by reading the instructions mentioned above.")