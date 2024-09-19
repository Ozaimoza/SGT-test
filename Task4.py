def graduation(gpa, total_credits, honors_credits):
    if total_credits < 180 or gpa < 2.0:
        return "not graduating"
    
    if gpa >= 3.8:
        return "summa cum laude" if honors_credits >= 15 else "magna cum laude"
    elif gpa >= 3.6:
        return "magna cum laude" if honors_credits >= 15 else "cum laude"
    else:
        return "graduating"


print(graduation(3.87, 178, 16))
print(graduation(1.5, 199, 30))
print(graduation(2.7, 380, 50))
print(graduation(3.62, 200, 20))
print(graduation(3.93, 185, 0))
print(graduation(3.85, 190, 15))