def facto(number):
    """Turns a variable into a factored number"""

    fact = 1
    for x in range(number,0,-1):
        fact *= x
        
    return fact  


print(f"The factorial of 12 is {facto(12)}")