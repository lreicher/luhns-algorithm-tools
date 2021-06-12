# lreicher 2021 - Luhn's Algorithm Tools
import random, sys

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

def get_random_card_by_type(type):
    if type == "visa":
        sum_digits = "4"
        sum_digits += str(random_with_N_digits(14))
    elif type == "mastercard":
        sum_digits = str(random.randint(51,55))
        sum_digits += str(random_with_N_digits(13))
    elif type == "amex":
        sum_digits = str(random.choice([34, 37]))
        sum_digits += str(random_with_N_digits(12))
    return sum_digits

def check_Luhn(number):
    length = len(number)
    total = int(number[length-1])
    parity = length % 2
    for i in range(0, length-1):
        digit = int(number[i])
        if i % 2 == parity:
            digit *= 2
        if digit > 9:
            digit -= 9
        total += digit
    return (total % 10) == 0

def generate_Luhn(type):
    sum_digits = get_random_card_by_type(type)
    return add_check_sum(sum_digits)

def add_check_sum(sum_digits):
    length = len(sum_digits)+1
    total = 0
    even = True
    for i in range(length-2, -1, -1):
        if even:
            num = str(int(sum_digits[i])*2)
            if len(num) == 2:
                num = int(num[0]) + int(num[1])
            total += int(num)
            even = not even
        else:
            total += int(sum_digits[i])
            even = not even
    check_digit = (total * 9) % 10
    sum_digits += str(check_digit)
    return sum_digits

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc == 2:
        gen_luhn = generate_Luhn(sys.argv[1])
        print(gen_luhn)
        print(check_Luhn(gen_luhn))
    else:
        print("usage: luhn.py type")
