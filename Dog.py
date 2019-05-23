"""
Note for those coming from Java: Python objects require an explicit
reference to "self", which is not a reserved keyword like "this" is in Java.
The reasoning for using "self", and why it is not a reserved keyword, can be found here:
http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html.
"""

class Dog:

    # A constructor
    def __init__(self, name, age):  # Now, each dog will keep track of its own name and age.
        self.name = name
        self.age = age

    # ~~~~ Getters ~~~~
    # Note: Getters and setters are the proper way to interface with an object's data.

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_age_in_dog_years(self):
        return self.age * 7

    # ~~~~ Instance methods ~~~~

    def bark(self):
        print(self.name + " barks.")

    def wag_tail(self):
        print(self.name + "'s tail is wagging.")

    def have_a_birthday(self):
        print("Happy birthday " + self.name + "!")
        self.age += 1
