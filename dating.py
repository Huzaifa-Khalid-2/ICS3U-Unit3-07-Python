#!/usr/bin/env python3

# Created by: Huzaifa
# Created on: March 2022
# This function asks a user if they are rich and handsome
# and depending on their answeres it tells if they can date
# the grandchild


def main():
    # This function asks a user if they are rich and handsome
    # and depending on their answeres it tells if they can date
    # the grandchild

    # input
    user_wealth = input("Are you rich?(yes or no): ")
    user_looks = input("Are you handsome?(yes or no): ")
    print("")

    # process and output
    if user_wealth == "yes" or user_looks == "yes":
        print("You can date the grandchild.")
    elif user_wealth == "no" and user_looks == "no":
        print("You can not date the grandchild.")
    else:
        print("Sorry big man I got nothing ¯\_(ツ)_/¯.")
        print("")
    print("Thanks for checking.")
    print("\nDone.")


if __name__ == "__main__":
    main()
