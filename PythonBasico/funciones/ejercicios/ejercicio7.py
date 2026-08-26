def find_prime_numbers(number_list):
    prime_numbers=[]
    for number in number_list:
        if is_prime_number(number):
            prime_numbers.append(number)
    return prime_numbers

def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(find_prime_numbers([1, 4, 6, 7, 13, 9, 67]))