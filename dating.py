#!/usr/bin/env python3

# Created by: Huzaifa
# Created on: April 2022
# This function asks a user if they are rich and handsome
# and depending on their answeres it tells if they can date
# the grandchild


def main():
    # This function asks a user if they are rich and handsome
    # and depending on their answeres it tells if they can date
    # the grandchild

    # input
    user_wealth = input("Are you rich?(yes or no): ")
    user_looking = input("Are you handsome?(yes or no): ")
    print("")

    # process and output
    if user_wealth == "yes" or user_looking == "yes":
        print("You can date the grandchild.")
    elif user_wealth == "no" and user_looking == "no":
        print("You can not date the grandchild.")
    else:
        print("Really? (-_-)ゞ all you had to do was say yes or no.")
        print("")

    print("\nDone.")


if __name__ == "__main__":
    main()
