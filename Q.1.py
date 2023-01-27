def is_perfect(num):
    divisors = []
    # find divisors of the given number
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    # check if the sum of divisors equal to the given number
    if sum(divisors) == num:
        return True
    return False

# test the function
print(is_perfect(6)) # True
print(is_perfect(28)) # True
print(is_perfect(496)) # True
print(is_perfect(8128)) # True
print(is_perfect(5)) # False
