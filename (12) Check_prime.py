def check_prime(s):
    if s <= 1:
        return False

    for i in range(2, int(s ** 0.5) + 1):
        if s % i == 0:
            return False

    return True

print(check_prime(25))
