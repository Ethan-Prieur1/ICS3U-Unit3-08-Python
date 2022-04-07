#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that checks if a certain year is a leap year


def main():
    # This function is the main program

    # Input
    year_as_string = input("Enter a Year: ")

    # Process & output

    try:
        year_as_int = int(year_as_string)
        if year_as_int % 4 == 0:
            if year_as_int % 100 == 0:
                if year_as_int % 400 == 0:
                    print("That IS a Leap Year! YAHOO!")
                else:
                    print("Aw Man, That's NOT a Leap Year!")
            else:
                print("That IS a Leap Year! YAHOO!")
        else:
            print("Aw Man, That's NOT a Leap Year!")
    except Exception:
        print("That is not an Integer")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
