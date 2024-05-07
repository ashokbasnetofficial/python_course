num = int(input("Please enter any number:"))

def prime_number_checker(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if prime_number_checker(num):
    print(f'{num} is a prime number.')
else:
    print(f'{num} is a composite number.')
