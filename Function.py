def is_prime(number):
    _isPrim = True
    for i in [2, 3, 5, 7]:
        if number%i==0:
            _isPrim=False
            break
    return _isPrim


print is_prime(input())