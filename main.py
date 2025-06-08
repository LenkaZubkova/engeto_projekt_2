"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Lenka Zubkova
email: lenka_zubkova@hotmail.com
"""

import random
import time

def generate_secret_number():
    """
    Vygeneruje náhodné 4místné číslo s unikátními číslicemi (1-9).
    :return: string, tajné číslo
    """
    digits = list("123456789")
    random.shuffle(digits)
    secret_number = digits[:4]
    return "".join(secret_number)

def is_valid_guess(guess):
    """
    Ověří, zda je vstup platný tip: 4 různé číslice, nezačíná nulou.
    :param guess: string
    :return: bool
    """
    if len(guess) != 4:
        return False
    if not guess.isdigit():
        return False
    if guess[0] == '0':
        return False
    if len(set(guess)) != 4:
        return False
    return True

def evaluate_guess(secret, guess):
    """
    Vyhodnotí tip uživatele a spočítá bulls a cows.
    :param secret: string, tajné číslo
    :param guess: string, tip uživatele
    :return: tuple (bulls, cows)
    """
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def print_intro():
    """
    Vytiskne úvodní zprávu pro uživatele.
    """
    print("Hi there!")
    print(47*"-")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(47*"-")

def main():
    print_intro()
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Enter a number: ")
        if not is_valid_guess(guess):
            print("Invalid input. Make sure your guess is a 4-digit number with unique digits and does not start with 0.")
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        if bulls == 4:
            end_time = time.time()
            duration = end_time - start_time
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(55*"-")
            print(f"That's amazing! It took you {duration:.2f} seconds.")
            break
        else:
            bulls_text = "bull" if bulls == 1 else "bulls"
            cows_text = "cow" if cows == 1 else "cows"
            print(f"{bulls} {bulls_text}, {cows} {cows_text}")
            print("-----------------------------------------------")

if __name__ == "__main__":
    main()