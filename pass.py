import re
weak_passwords = ['password', '123456', 'qwerty', 'abc123', 'admin', 'letmein']

def check_password_strength(password):
    score = 0
    
    if password.lower() in weak_passwords:
        return "Very Weak (Common password)"
    
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[\W_]', password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"


while True:
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print("Strength:", strength)
    
    if strength == "Strong":
        break  
    else:
        print("Try again with a stronger password.\n")
