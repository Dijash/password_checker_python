
def pass_checker(password):
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-+"
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    score = 0
    if length >= 5:
        score +=1
    if has_upper:
        score+=1
    if has_lower:
        score+=1
    if has_digit:
        score+=1
    if has_special:
        score+=1
        
    if score<2:
        return"u gay bitch"
    elif score >=2 and score<=4:
        return"u little gay boi"
    elif score>=5:
        return"u no gay boi"
    else:
        return"go fuck yourself"
        
password = input("Enter password: ")        
result = pass_checker(password)
print("u fkin bitch u pass is dis",result)                  
            
            
        