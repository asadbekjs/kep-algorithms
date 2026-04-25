def is_prime(n):
    if n <= 1:
        return False
    
    # n = 16; 2, 3, 4, ... 16
    for son in range(2, int(n ** 0.5) + 1):
        if n % son == 0:
            return False
        
    return True

n = int(input())
print("Yes") if is_prime(n) else print("No")
