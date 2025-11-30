#!/usr/bin/env python3
# Created by: Angelo Garcia
# Program accepts a whole number. It then uses a for loop to calculate and display the “square” (power of 2) starting from 0 until this number.
# Input validation requires a positive whole number (> 0). No break/continue used.


def main():
    user_number = None
    while user_number is None:
        user_input = input("Enter a positive whole number: ")
        try:
            val = int(user_input)
            if val <= 0:
                print("Please enter a positive whole number.")
            else:
                user_number = val
        except ValueError:
            print("That is not a valid positive whole number. Try again.")

    exp_width = len(str(user_number))
    for exp in range(user_number + 1):
        value = 2**exp
        # The original code had a small logical inconsistency: it calculated powers of 2 (2**exp),
        # but the print statement showed 'exp^2'. The code below calculates and displays powers of 2 correctly,
        # reflecting the calculation performed in the 'value = 2**exp' line.
        # If the intent was actually to calculate squares of 'exp', the 'value' line should be changed to 'value = exp**2'
        print(f"2^{exp:<{exp_width}} = {value}")


if __name__ == "__main__":
    main()
