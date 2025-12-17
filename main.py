def pass_checker(password):
    score = 0
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-+"
    result = ['Weak','Medium','Strong','Error']
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
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
        strength = result[0]
    elif score >=2 and score<=4:
        strength = result[1]
    elif score>=5:
        strength = result[2]
    else:
        strength = result[3]
    
    return score, strength
 
password = input("Enter password: ")        
score,result = pass_checker(password)
print("Your password is",result) 
print("Your password score is "+str(score)+"/5")                 
            
            
        