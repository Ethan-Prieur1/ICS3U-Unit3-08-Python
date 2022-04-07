#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that checks if a certain year is a leap year


def main():
    # This function is the main program

    # Input
    year = int(input("Enter a Year: "))

    # Process & output

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("That IS a Leap Year! YAHOO!")
            else:
                print("Aw Man, That's NOT a Leap Year!")
        else:
            print("That IS a Leap Year! YAHOO!")
    else:
        print("Aw Man, That's NOT a Leap Year!")
    print("\nDone.")


if __name__ == "__main__":
    main()
