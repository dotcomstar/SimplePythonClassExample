#!/usr/bin/env python
import os
import sys
from Dog import *  # Imports everthing from the Dog class into this file.

def main():
    print("Starting main()\n")

    fido = Dog("Fido", 3)  # Instantiates a new Dog object

    print("Hello, my name is " + fido.get_name())
    print("I am " + str(fido.get_age()) + " years old.")
    print("I am " + str(fido.get_age_in_dog_years()) + " years old in dog years.\n")

    fido.bark()
    fido.wag_tail()
    print("")  # Adds a new-line to output for readability

    print("Now it is my birthday.")
    fido.have_a_birthday()
    print("Now, I am " + str(fido.get_age()) + " years old.")
    print("And I am " + str(fido.get_age_in_dog_years()) + " years old in dog years.\n")

    print("Finished main()")

# ~~~~ Don't worry about this for now ~~~~
if __name__ == "__main__":
    main()
