# lreicher 2021 - Luhn's Algorithm Tools
import random, sys

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

def get_random_card_by_type(type):
    sum_digits = ""
    if type == "visa":
        sum_digits = "4" + str(random_with_N_digits(14))
    elif type == "mastercard":
        sum_digits = str(random.randint(51,55)) + str(random_with_N_digits(13))
    elif type == "amex":
        sum_digits = str(random.choice([34, 37])) + str(random_with_N_digits(12))
    return sum_digits

def sum_digits(number, length):
    total = 0
    parity = length % 2
    for i in range(0, length-1):
        digit = int(number[i])
        if i % 2 == parity:
            digit *= 2
        if digit > 9:
            digit -= 9
        total += digit
    return total

def check_Luhn(number):
    length = len(number)
    total = int(number[length-1]) + sum_digits(number, length)
    return (total % 10) == 0

def generate_Luhn(type):
    sum_digits = get_random_card_by_type(type)
    return add_check_sum(sum_digits)

def add_check_sum(number):
    total = sum_digits(number, len(number)+1)
    check_digit = (total * 9) % 10
    return number + str(check_digit)

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc == 3:
        if sys.argv[1] == '-v':
            print(check_Luhn(sys.argv[2]))
        elif sys.argv[1] == '-c':
            print(generate_Luhn(sys.argv[2]))
        else:
            print("usage: luhn.py type")
    else:
        print("usage: luhn.py type")
