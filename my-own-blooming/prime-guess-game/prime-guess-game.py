import math
from random import random


def get_random_number(min: int = 1, max: int = 100) -> int:
    '''
    Returns random number in optional range
    default is min = 1 and max = 100.
    '''
    number: int = math.floor(random() * (max - min + 1)) + min
    return number


def is_number_prime(number: int) -> bool:
    '''
    Determines whether a number is prime
    in a O(sqrt(n)) complexity time and
    return boolean True or False.
    '''
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    print("Welcome to the Prime Guess Game!")
    username: str = input("May i have your name? ")
    print("Hello, %s!" % username)
    print("Answer 'yes' if the number is prime, otherwise answer 'no'")

    for i in range(0, 3):
        random_number: int = get_random_number(1, 100)
        true_answer: str = 'yes' if is_number_prime(random_number) else 'no'
        user_answer: str = input("Is %s a prime number?\n" % random_number)
        if user_answer != true_answer:
            print("Try again!")
            quit()
        print("Good job!")


if __name__ == '__main__':
    main()
