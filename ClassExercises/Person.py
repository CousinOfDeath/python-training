import datetime


class Person:
    def __init__(self, first_name, last_name, year):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        """Use datetime module"""
        return datetime.date.today().year - self.year

    def __str__(self):
        return f"{self.full_name()} is {self.age()} years old"


p = Person("Cousin", "Death", 1982)

print(p)